import React from 'react';
import logoImage from '../splittextalone.png';

const styles = {
  navbar: {
    backgroundColor: '#ededed',
    height: '50px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '0 50px',
  },
  logo: {
    cursor: 'pointer',
  },
  logoImage: {
    height: '40px',
    width: 'auto',
  },
  navbarNav: {
    listStyle: 'none',
    display: 'flex',
    gap: '20px',
  },
  navItem: {
    height: '60px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  navLink: {
    textDecoration: 'none',
    color: 'black',
    fontSize: '16px',
    fontFamily: 'Arial, sans-serif',
    fontWeight: 'bold',
    transition: 'color 0.3s ease',
    display: 'block',
    padding: '0 10px',
    width: '120px',
    opacity: 1,
  },
  navLinkHover: {
    color: '#305E48',
    cursor: 'pointer',
    opacity: 1,
  },
  spanStyle: {
    display: 'inline-block'
  },
};

const Navbar = () => {
  const [hoveredLink, setHoveredLink] = React.useState(null);
  const [logoHovered, setLogoHovered] = React.useState(false);

  const splitLetters = (word) => {
    return [...word].map((letter, i) => (
      <span
        key={i}
        className={logoHovered || hoveredLink === word ? "animate-text" : ""}
      >
        {letter}
      </span>
    ));
  };

  return (
    <nav style={styles.navbar}>
      <div
        style={styles.logo}
        onMouseEnter={() => setLogoHovered(true)}
        onMouseLeave={() => setLogoHovered(false)}
      >
        <a href="/Home" style={{ textDecoration: 'none' }}>
          <img src={logoImage} alt="Logo" style={styles.logoImage} />
        </a>
      </div>
      <ul style={styles.navbarNav}>
        <li style={styles.navItem}>
          <a
            href="/Home"
            className="nav-link"
            onMouseEnter={() => setHoveredLink('Home')}
            onMouseLeave={() => setHoveredLink(null)}
            style={
              hoveredLink === 'Home'
                ? { ...styles.navLink, ...styles.navLinkHover }
                : { ...styles.navLink }
            }
          >
            {splitLetters('Home')}
          </a>
        </li>
        <li style={styles.navItem}>
          <a
            href="/Message"
            className="nav-link"
            onMouseEnter={() => setHoveredLink('Message')}
            onMouseLeave={() => setHoveredLink(null)}
            style={
              hoveredLink === 'Message'
                ? { ...styles.navLink, ...styles.navLinkHover }
                : { ...styles.navLink }
            }
          >
            {splitLetters('Message')}
          </a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
