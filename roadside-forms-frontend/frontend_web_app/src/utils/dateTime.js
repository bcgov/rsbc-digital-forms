export const getCurrentDateTime = () => {
    const now = new Date();
    const dayString = now.toLocaleDateString('en-CA', { weekday: 'long' });
    const dateString = now.toLocaleDateString('en-CA');
    const pacificTime = now.toLocaleTimeString('en-CA', { timeZone: 'America/Vancouver', hour12: false });
    const timeString = pacificTime.substr(0, 5);
    return { dateString, dayString, timeString };
  };
  