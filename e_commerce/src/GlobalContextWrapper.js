import { useState , useEffect} from "react";
import { GlobalContext } from "./GlobalContext";

export default function GLobalContectWrapper(props){

    const [products, setProducts] = useState([]);
    const [cart, setCart] = useState({});

    function changeProducts(value) {
        setProducts(value) 
    }

    function changeCart(value){
        setCart(value);
    }

    useEffect(() => {
        fetch("https://fakestoreapi.com/products")
                      .then((res) => res.json())
                      .then((json) => {
                          setProducts(json)
                      });
        // console.log(products);
      },[])

    return(
        <GlobalContext.Provider value={{products: products, changeProducts: changeProducts, cart: cart, changeCart: changeCart}}>
            {props.children}
        </GlobalContext.Provider>
    )
}