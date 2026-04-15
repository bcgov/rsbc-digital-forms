import React from "react";
import {
  Navigate,
  Route,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";
import { Login } from "../components/Login/login";
import { Layout } from "../components/common/Layout/Layout";

export const appRouter = createBrowserRouter(
  createRoutesFromElements(
    <Route element={<Layout />}>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route path="*" element={<Navigate to="/login" />} />
    </Route>
  ),
  {
    basename: "/roadside-forms",
  }
);
