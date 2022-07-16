import { useContext, useEffect, useState } from "react";
import { GlobalContext } from "./GlobalContext";
import AddToCart from "./AddToCart";
import './Home.css';

import { Link } from "react-router-dom";

export default function CartPage(){
    const {products, cart, changeCart} = useContext(GlobalContext);
    let items = [];
    // const [items, setItems] = useState([]);
    // useEffect(() =>{
        // if(products.length === 0){
        //     // return(
        //     //     <div></div>
        //     // )
        // }
        // else{
            items = [];
            for(let [key, value] of Object.entries(cart)){
                let x = products[key - 1];
                // console.log(x);
                items.push(
                    <div className="product">
                        <div className="productIMG">
                            <img className="qwe" src={x.image} alt="asdf"></img>
                        </div>
                        <div className="productInfo">
                            <div>{x.title}</div>
                            <div>Price: {x.price}</div>
                            <div>Category: {x.category}</div>
                            <div>Rating: {x.rating.rate}</div>
                            <AddToCart id={x.id} quantity={value}/>
                        </div>
                    </div>
                )   
            // }
            // setItems(tempC);
        }
    // });
    return(
        <div>
        <div className = "header">
                FlipMart
                <div>
                    <Link to="/cart">
                        <button className="cart-btn">Cart</button>
                    </Link>
                </div>
            </div>
        <div className="productList">{items}</div>
        {/* <button className="order">Place Order</button> */}
        </div>
    );
}