import React from "react";
import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";
import { Login } from "../components/Login/login";
import { Dashboard } from "../components/Dashboard/Dashboard";
import { PrivateRoutes } from "./PrivateRoutes";
import { RequestAccess } from "../components/RequestAccess/requestAccess";
import { UserAdminDashboard } from "../components/userAdminDashboard/userAdminDashboard";
import { CreateEvent } from "../components/Event/createEvent";
import { ViewPastEvent } from "../components/ViewPastEvent/viewPastEvent";
import { Layout } from "../components/common/Layout/Layout";

export const appRouter = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<Layout />}>
      <Route path="/login" element={<Login />} />
      <Route path="/requestAccess" element={<RequestAccess />} />
      <Route element={<PrivateRoutes />}>
        <Route path="/createEvent" element={<CreateEvent />} />
        <Route index element={<Dashboard />} exact />
        <Route path="/admin-console" element={<UserAdminDashboard />} exact />
        <Route path="/view-previous" element={<ViewPastEvent />} exact />
      </Route>
    </Route>
  ),
  {
    basename: "/roadside-forms",
  }
);
