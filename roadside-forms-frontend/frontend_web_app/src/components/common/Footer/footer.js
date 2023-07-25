import React from 'react';
import packageJson from '../../../../package.json';

export const Footer = () => {
  return (
    <footer id="roadesafety-footer" className='text-center text-font'>
      <p>Version: {packageJson.version}</p>
    </footer>
  );
}
