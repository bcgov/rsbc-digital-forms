import React, { useState } from "react";
import CloseIcon from "@mui/icons-material/Close";
import "./retirementBanner.scss";

export const RetirementBanner = () => {
  const [isVisible, setIsVisible] = useState(true);

  const handleClose = () => {
    setIsVisible(false);
  };

  if (!isVisible) {
    return null;
  }

  return (
    <div className="retirement-banner" role="alert">
      <div className="retirement-banner-content">
        <div className="retirement-banner-text">
          <div className="retirement-banner-title">
            <strong>Important Notice:</strong> The new Digital Forms website is available right now.
          </div>
          <div className="retirement-banner-message">
            This legacy version of Roadside Forms will be retired on <strong>18 December 2025</strong>. 
            Please complete and submit all forms before this date. Copies of a submitted form can be 
            requested from ICBC (12h/24h) or RSBC (VI).
          </div>
        </div>
        <div className="retirement-banner-actions">
          <a 
            href="https://jag.gov.bc.ca/digital-forms-v3/" 
            target="_blank" 
            rel="noopener noreferrer"
            className="retirement-banner-button"
          >
            Visit New Digital Forms Website →
          </a>
          <button 
            className="retirement-banner-close"
            onClick={handleClose}
            aria-label="Close banner"
            type="button"
          >
            <CloseIcon />
          </button>
        </div>
      </div>
    </div>
  );
};
