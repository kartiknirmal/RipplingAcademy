import { useContext, useEffect, useState } from "react";
import { GlobalContext } from "./GlobalContext";
import AddToCart from "./AddToCart";
import './Home.css';
import { Link } from "react-router-dom";

export default function Home() {
    const {products, cart} = useContext(GlobalContext);
    const [electronicsFilter, setElectronicsFilter] = useState(true);
    const [jeweleryFilter, setJeweleryFilter] = useState(true);
    const [menClothFilter, setMenClothFilter] = useState(true);
    const [womenClothFilter, setWomenClothFilter] = useState(true);

    const [categoryArray, setCategoryArray] = useState({"electronics":true, "jewelery":true, "men's clothing":true, "women's clothing":true});


    function onChangeElectronics() {
        setElectronicsFilter(!electronicsFilter);
        let tempC = JSON.parse(JSON.stringify(categoryArray));
        tempC["electronics"] = !tempC["electronics"];
        setCategoryArray(tempC);
        // console.log("jfejn", categoryArray["electronics"]);
    }

    function onChangeJewelery() {
        setJeweleryFilter(!jeweleryFilter);
        let tempC = JSON.parse(JSON.stringify(categoryArray));
        tempC["jewelery"] = !tempC["jewelery"];
        setCategoryArray(tempC);
        // categoryArray["jewelery"] = !categoryArray["jewelery"];
    }

    function onChangeMenCloth() {
        setMenClothFilter(!menClothFilter);
        let tempC = JSON.parse(JSON.stringify(categoryArray));
        tempC["men's clothing"] = !tempC["men's clothing"];
        setCategoryArray(tempC);
        // categoryArray["men's clothing"] = !categoryArray["men's clothing"];
    }

    function onChangeWomenCloth() {
        setWomenClothFilter(!womenClothFilter);
        let tempC = JSON.parse(JSON.stringify(categoryArray));
        tempC["women's clothing"] = !tempC["women's clothing"];
        setCategoryArray(tempC);
        // categoryArray["women's clothing"] = !categoryArray["women's clothing"];
    }

    // console.log(products);
    const items = [];
    // useEffect(()=>{
    //     for(let i = 0; i < products.length; i++){
    //         if(categoryArray[products[i].category]){
    //             items.push(
    //                 <div className="product">
    //                     <div className="productIMG">
    //                         <img className="qwe" src={products[i].image} alt="asdf"></img>
    //                     </div>
    //                     <div className="productInfo">
    //                         <div>{products[i].title}</div>
    //                         <div>Price: {products[i].price}</div>
    //                         <div>Category: {products[i].category}</div>
    //                         <div>Rating: {products[i].rating.rate}</div>
    //                         <AddToCart id={products[i].id} quantity={products[i].id in cart ? cart[products[i].id] : 0}/>
    //                     </div>
    //                 </div>
    //             )
    //         }
    //     }
    // }, [categoryArray, products])
    for(let i = 0; i < products.length; i++){
        // console.log(categoryArray["electronics"]);
        if(categoryArray[products[i].category]){
            items.push(
                <div className="product">
                    <div className="productIMG">
                        <img className="qwe" src={products[i].image} alt="asdf"></img>
                    </div>
                    <div className="productInfo">
                        <div>{products[i].title}</div>
                        <div>Price: {products[i].price}</div>
                        <div>Category: {products[i].category}</div>
                        <div>Rating: {products[i].rating.rate}</div>
                        <AddToCart id={products[i].id} quantity={products[i].id in cart ? cart[products[i].id] : 0}/>
                    </div>
                </div>
            )
        }
    }
    // console.log(items.length)
    // const items1 = products.map((x) => 
    //     <div className="product">
    //         <div className="productIMG">
    //             <img className="qwe" src={x.image} alt="asdf"></img>
    //         </div>
    //         <div className="productInfo">
    //             <div>{x.title}</div>
    //             <div>Price: {x.price}</div>
    //             <div>Category: {x.category}</div>
    //             <div>Rating: {x.rating.rate}</div>
    //             <AddToCart id={x.id} quantity={x.id in cart ? cart[x.id] : 0}/>
    //         </div>
    //     </div>
    // );
    // const items = products.map((x) => <li>{x.id}</li>);
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
            <form onSubmit={()=>{}}>
                <div className="form-check">
                    <label className="form-check-label">
                    <input type="checkbox"
                        checked={electronicsFilter}
                        onChange={onChangeElectronics}
                        className="form-check-input"
                    />
                    electronics
                    </label>
                </div>
                <div className="form-check">
                    <label className="form-check-label">
                    <input type="checkbox"
                        checked={jeweleryFilter}
                        onChange={onChangeJewelery}
                        className="form-check-input"
                    />
                    jewelery
                    </label>
                </div>
                <div className="form-check">
                    <label className="form-check-label">
                    <input type="checkbox"
                        checked={menClothFilter}
                        onChange={onChangeMenCloth}
                        className="form-check-input"
                    />
                    men's clothing
                    </label>
                </div>
                <div className="form-check">
                    <label className="form-check-label">
                    <input type="checkbox"
                        checked={womenClothFilter}
                        onChange={onChangeWomenCloth}
                        className="form-check-input"
                    />
                    women's clothing
                    </label>
                </div>
            </form>

            <div className="productList">
                {items}
            </div>
        </div>
    )
}