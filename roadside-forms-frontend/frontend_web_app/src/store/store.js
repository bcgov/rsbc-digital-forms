import { configureStore } from "@reduxjs/toolkit";

import rootReducer from "./reducers";

export default configureStore({
  reducer: rootReducer,
  preloadedState: {
    serviceWorkerInitialized: false,
    serviceWorkerUpdated: false,
    serviceWorkerRegistration: null,
  },
});
