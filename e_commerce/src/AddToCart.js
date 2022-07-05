import { useContext, useState } from "react"
import { GlobalContext } from "./GlobalContext";

export default function AddToCart(props){
    let [quantity, setQuantity] = useState(props.quantity);
    const {cart, changeCart} = useContext(GlobalContext);
    // console.log(props.quantity);
    function incrementQuantity() {
        quantity = quantity + 1;
        setQuantity(quantity);
        let tempCart = cart;
        tempCart[props.id] = quantity;
        changeCart(tempCart);
    }
    function decrementQuantity() {
        quantity = quantity - 1;
        setQuantity(quantity);
        if(quantity === 0){
            // let tempCart = cart;
            let tempCart = JSON.parse(JSON.stringify(cart))
            delete tempCart[props.id];
            changeCart(tempCart);
        }
        else{
            let tempCart = cart;
            tempCart[props.id] = quantity;
            changeCart(tempCart);
        }
    }
    if(quantity === 0){
        return(
            <button onClick={incrementQuantity}>Add to Cart</button>
        )
    }
    return (
        <div>
            <button onClick={decrementQuantity}>-</button>
            {quantity}
            <button onClick={incrementQuantity}>+</button>
        </div>
    );
}