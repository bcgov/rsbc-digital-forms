/* eslint-disable no-restricted-globals */

import { clientsClaim } from "workbox-core";
import { ExpirationPlugin } from "workbox-expiration";
import { BackgroundSyncPlugin } from "workbox-background-sync";
import { precacheAndRoute, createHandlerBoundToURL } from "workbox-precaching";
import { registerRoute } from "workbox-routing";
import {
  StaleWhileRevalidate,
  CacheFirst,
  NetworkOnly,
} from "workbox-strategies";
import { CacheableResponsePlugin } from "workbox-cacheable-response";

clientsClaim();

// Precache all of the assets generated by your build process.
// Their URLs are injected into the manifest variable below.
// This variable must be present somewhere in your service worker file,
// even if you decide not to use precaching.
const manifest = (self.__WB_MANIFEST || []).concat([
  {
    url: "/roadside-forms/",
    revision: null,
  },
  // {
  //     url: "/roadside-forms/static/media/BCID_RoadSafetyBC_logo_transparent.png",
  //     revision: null,
  //   },
  {
    url: "/roadside-forms/assets/libre-barcode-39-v19-latin-regular.woff",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2634E_082023_driver.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2634E_082023_icbc.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2634E_082023_ilo.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2721_201502_appeal.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2721_201502.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2722_201502_Incident_Details.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2722_201502.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2906E_082023_driver.png",
    revision: null,
  },
  {
    url: "/roadside-forms/assets/MV2906E_082023_icbc.png",
    revision: null,
  },
  // {
  //   url: "/roadside-forms/createEvent",
  //   revision: null,
  // },
  // Add other assets to cache here
]);
precacheAndRoute(manifest);

// Set up App Shell-style routing, so that all navigation requests
// are fulfilled with your index.html shell. Learn more at
// https://developers.google.com/web/fundamentals/architecture/app-shell
const fileExtensionRegexp = new RegExp("/[^/?]+\\.[^/]+$");
registerRoute(
  // Return false to exempt requests from being fulfilled by index.html.
  ({ request, url }) => {
    // If this isn't a navigation, skip.
    if (request.mode !== "navigate") {
      return false;
    } // If this is a URL that starts with /_, skip.

    if (url.pathname.startsWith("/_")) {
      return false;
    } // If this looks like a URL for a resource, because it contains // a file extension, skip.

    if (url.pathname.match(fileExtensionRegexp)) {
      return false;
    } // Return true to signal that we want to use the handler.

    return true;
  },
  createHandlerBoundToURL(process.env.PUBLIC_URL + "/index.html")
);

// This allows the web app to trigger skipWaiting via
// registration.waiting.postMessage({type: 'SKIP_WAITING'})
self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "SKIP_WAITING") {
    self.skipWaiting();
  }
});

self.addEventListener("waiting", (event) => {
  if (confirm("A new version is available. Do you want to update?")) {
    self.skipWaiting();
  }
});

// Any other custom service worker logic can go here.

registerRoute(
  // Check to see if the request's destination is style for stylesheets, script for JavaScript, or worker for web worker
  ({ request }) =>
    request.destination === "style" ||
    request.destination === "script" ||
    request.destination === "worker",
  // Use a Stale While Revalidate caching strategy
  new StaleWhileRevalidate({
    // Put all cached files in a cache named 'assets'
    cacheName: "assets",
    plugins: [
      // Ensure that only requests that result in a 200 status are cached
      new CacheableResponsePlugin({
        statuses: [200],
      }),
    ],
  })
);

registerRoute(
  ({ url }) =>
    url.pathname.includes("/api/v1/static/agencies") ||
    url.pathname.includes("/api/v1/static/cities") ||
    url.pathname.includes("/api/v1/static/configuration") ||
    url.pathname.includes("/api/v1/static/countries") ||
    url.pathname.includes("/api/v1/static/jurisdictions") ||
    url.pathname.includes("/api/v1/static/provinces") ||
    url.pathname.includes("/api/v1/static/vehicles") ||
    url.pathname.includes("/api/v1/static/vehicle_styles"),
  new CacheFirst({
    cacheName: "static-api",
    plugins: [
      // Ensure that only requests that result in a 200 status are cached
      new CacheableResponsePlugin({
        statuses: [200],
      }),
      new ExpirationPlugin({
        maxAgeSeconds: 60 * 60 * 24 * 2, // 2 Days
      }),
    ],
  })
);

registerRoute(
  ({ url }) =>
    url.pathname.includes("/api/v1/static/impound_lot_operators") ||
    url.pathname.includes("/api/v1/users") ||
    url.pathname.includes("/api/v1/user_roles"),
  new StaleWhileRevalidate({
    cacheName: "dynamic-api",
    plugins: [
      // Ensure that only requests that result in a 200 status are cached
      new CacheableResponsePlugin({
        statuses: [200],
      }),
    ],
  })
);

registerRoute(
  ({ url }) => url.pathname.includes("/api/v1/event"),
  new NetworkOnly({
    plugins: [
      new BackgroundSyncPlugin("roadside-forms-event", {
        maxRetentionTime: 24 * 60, // Retry for max of 24 Hours (specified in minutes)
      }),
    ],
  }),
  "POST"
);

registerRoute(
  ({ url }) => url.pathname.includes("/api/v1/forms"),
  new NetworkOnly({
    plugins: [
      new BackgroundSyncPlugin("roadside-forms-id", {
        maxRetentionTime: 24 * 60, // Retry for max of 24 Hours (specified in minutes)
      }),
    ],
  }),
  "PATCH"
);

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
