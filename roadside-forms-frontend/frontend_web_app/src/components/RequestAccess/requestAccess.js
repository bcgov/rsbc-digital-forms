import React from 'react';
import { Button } from '../Button/Button';

export const RequestAccess= () => {
  return (
    <div className='border-design text-font'>
        <p>
          <span className="fw-bold">Welcome to the Digital Forms system</span>
        </p>
        <p>
          <em>WARNING: This system is for use by authorized law enforcement officers only.</em>
        </p>
        <p>
          You currently do not have access to the Digital Forms system.
        </p>
        <p>
          Please apply for access after completing the training course and with the approval of your unit commander.
        </p>
      <Button primary size="large" label="Apply for Access" />
    </div>
  );
}
