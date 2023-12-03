import React from "react";
import ReactDOM from "react-dom/client";
import Inicio from "./Inicio.jsx";
import "./index.css";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Inicio />,
  },
/*   {
    path: "/Inicio",
    element: <IniciarSesion />,
  },
  {
    path: "/registrarse",
    element: <Registrarse />,
  }, */
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
