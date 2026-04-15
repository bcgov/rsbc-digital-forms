import "./retirementBanner.scss";

export const RetirementBanner = () => {
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
            <div className="retirement-banner-actions">
              <a 
                href="https://jag.gov.bc.ca/digital-forms/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="retirement-banner-button"
              >
                Visit New Digital Forms Website →
              </a>
            </div>            
            <p>Please update your Digital Forms website shortcut or bookmark:</p>
            <a href="https://jag.gov.bc.ca/digital-forms/" target="_blank" rel="noopener noreferrer">
              https://jag.gov.bc.ca/digital-forms/
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};
