import React from "react";
import { Header } from "../Header/Header";
import { Outlet } from "react-router";
import { Footer } from "../Footer/footer";
import { RetirementBanner } from "../Banner/RetirementBanner";

export const Layout = () => {
  return (
    <div>
      <Header />
      <RetirementBanner />
      <Outlet />
      <Footer />
    </div>
  );
};
