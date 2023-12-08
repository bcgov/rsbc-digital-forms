import { useState, useEffect } from "react";
import { useBetween } from "use-between";

const useIsOnline = () => {
  const [isConnected, setIsConnected] = useState(navigator.onLine);

  useEffect(() => {
    const handleOnline = () => setIsConnected(true);
    const handleOffline = () => setIsConnected(false);

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);
    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, []);

  return {
    isConnected,
  };
};

export const useSharedIsOnline = () => useBetween(useIsOnline);
