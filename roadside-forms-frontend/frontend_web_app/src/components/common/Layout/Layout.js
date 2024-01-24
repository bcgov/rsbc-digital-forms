import React from "react";
import { Header } from "../Header/Header";
import { Outlet } from "react-router";
import { Footer } from "../Footer/footer";

export const Layout = () => {
  return (
    <div>
      <Header />
      <Outlet />
      <Footer />
    </div>
  );
};
