import React,{useState} from 'react';
import packageJson from '../../../../package.json';

export const Footer = () => {
  // code to on hover over <p> show another <p> element
  const [show, setShow] = useState(false);
  const hashValue = process.env.REACT_APP_GIT_COMMIT_HASH;
  const showText = () => setShow(true);
  const hideText = () => setShow(false);

  return (
    <footer id="roadesafety-footer" className='text-center text-font'>
      <p onMouseOver={showText} onMouseOut={hideText}>Version: {packageJson.version}</p>
      { show && <p>Hash: {hashValue}</p>}
    </footer>
  );
}
