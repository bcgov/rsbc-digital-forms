import React from "react";
// import ReactDOM from 'react-dom/client';
import ReactDOM from "react-dom";
import { RecoilRoot } from "recoil";
import "bootstrap/dist/css/bootstrap.css";
import App from "./App";
import * as serviceWorkerRegistration from "./serviceWorkerRegistration";
import reportWebVitals from "./reportWebVitals";
import store from "./store/store";
import { SW_INIT, SW_UPDATE } from "./constants/types";
import { Provider } from "react-redux";

// const root = ReactDOM.createRoot(document.getElementById('root'));
ReactDOM.render(
  <Provider store={store}>
    <RecoilRoot>
      <App />
    </RecoilRoot>
  </Provider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://cra.link/PWA
// serviceWorkerRegistration.unregister();
serviceWorkerRegistration.register({
  onSuccess: () => store.dispatch({ type: SW_INIT }),
  onUpdate: (registration) =>
    store.dispatch({ type: SW_UPDATE, payload: registration }),
});

// Catch routes like /roadside-blueberry/ and redirect to /roadside-forms/
if (!window.location.pathname.includes("/roadside-forms")) {
  window.location.replace("/roadside-forms");
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
