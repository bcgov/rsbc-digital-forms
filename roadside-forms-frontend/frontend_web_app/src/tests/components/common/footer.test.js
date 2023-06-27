import { render, screen } from '@testing-library/react';
import {Footer} from "../../../components/common/Footer/footer"

describe('Footer component', () => {
  test('renders version information', () => {
    render(<Footer />);
    const footerElement = screen.getByRole('contentinfo'); // 'contentinfo' is the ARIA role for footer elements
    const versionPattern = /Version: \d+\.\d+\.\d+/;
    
    expect(versionPattern.test(footerElement.textContent)).toBe(true);
  });
});
  
  
  
  
  
