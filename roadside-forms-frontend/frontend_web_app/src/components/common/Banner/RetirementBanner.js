import { useEffect, useState } from "react";

import "./retirementBanner.scss";

const REDIRECT_URL = "https://jag.gov.bc.ca/digital-forms/";
const REDIRECT_DELAY_SECONDS = 5;

export const RetirementBanner = () => {
  const [countdown, setCountdown] = useState(REDIRECT_DELAY_SECONDS);

  useEffect(() => {
    const intervalId = window.setInterval(() => {
      setCountdown((currentCountdown) => {
        if (currentCountdown <= 1) {
          window.clearInterval(intervalId);
          return 0;
        }

        return currentCountdown - 1;
      });
    }, 1000);

    const timeoutId = window.setTimeout(() => {
      window.location.assign(REDIRECT_URL);
    }, REDIRECT_DELAY_SECONDS * 1000);

    return () => {
      window.clearInterval(intervalId);
      window.clearTimeout(timeoutId);
    };
  }, []);

  return (
    <div className="retirement-banner" role="alert">
      <div className="retirement-banner-content">
        <div className="retirement-banner-text">
          <div className="retirement-banner-title">
            <strong>Important Notice:</strong> The new Digital Forms website is available now.
          </div>
          <div className="retirement-banner-message">
            <p>
              This legacy version of Roadside Forms is no longer available. 
              Please proceed to the new Digital Forms website to submit a Digital Form. 
              Copies of submitted forms can be requested from ICBC (12h/24h) or RSBC (VI).
            </p>
            <p className="retirement-banner-redirect-notice">
              You will be redirected automatically in <strong>{countdown}</strong>{" "}
              second{countdown === 1 ? "" : "s"}.
            </p>
            <div className="retirement-banner-actions">
              <a 
                href={REDIRECT_URL}
                target="_blank" 
                rel="noopener noreferrer"
                className="retirement-banner-button"
              >
                Visit New Digital Forms Website →
              </a>
            </div>            
            <p>Please update your Digital Forms website shortcut or bookmark:</p>
            <a href={REDIRECT_URL} target="_blank" rel="noopener noreferrer">
              {REDIRECT_URL}
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};
