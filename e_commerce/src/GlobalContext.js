import { createContext } from "react";

export const GlobalContext = createContext({products :[], changeProducts : () => {}, cart :{}, changeCart :() => {}});