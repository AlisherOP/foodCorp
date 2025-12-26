import { useState,useEffect } from "react"
import api from "../api"
import Item from "../components/Item.jsx"
import "../styles/Home.css"
function Home(){
    // keeping track of all the notes
    const [items, setItems]=useState([]);
    // create a new items
    const [item_name, setItemName] = useState("");
    const [item_desc, setItemDesc] = useState("");
    const [item_price, setItemPrice] = useState(0);
    const [item_cal, setItemCal] = useState(0);
    
    useEffect( () => {
        getItems();
    }, []);

    // This function fetches a list of notes from the server, stores them in the application's state using setItems
    const getItems = () => {
        api.get("/api/notes/").then((res) => res.data).then((data) => {setItems(data); console.log(data); 
        }).catch((err) => alert (err));
    };

    // to delete a notes
    const deleteItem=(id)=> {
        api.delete(`/api/notes/delete/${id}/`).then(
            // 204=successfully deleteing
            (res)=>{ if (res.status===204) alert("Item was deleted")
                    else alert("Failed to delete the item.")
                    getItems();
            }).catch((error) => alert(error));
    };

// createing items
    const createItem= (e) =>{
        e.preventDefault(); 
        api.post("/api/notes/", {
            item_name,
            item_desc,
            item_price,
            item_cal
        }).then((res) => {
            // its is created
            if (res.status===201) {alert("Item was created successfully");
            setItemName("");
            setItemDesc("");
            setItemPrice(0);
            setItemCal(0);
            } else alert("Failed to create an Item")
            getItems(); 
        }).catch((error) => alert(error));
    };
    return (<div> 
        <div>


            <h2>Items</h2>
            {items.map((item) => (
                <Item item={item} onDelete={deleteItem} key={item.id }/>
            ))}


        </div>
        <h2>Create an Item</h2>
        <form  onSubmit={createItem}>
            <label htmlFor="item_name">Item Name:</label>
        <br />
        <input 
        type="text" 
        id="item_name" 
        name="item_name" 
        required onChange = {(e) => setItemName(e.target.value)} 
        value={item_name}
        />
        <label htmlFor="item_desc">Item Desc:</label>
        <br />
        <textarea 
            name="item_desc" 
            id="item_desc" 
            required 
            value={item_desc} 
            onChange={(e) => setItemDesc(e.target.value)}>
        </textarea>
        <br />

        <label htmlFor="item_price">Item Price:</label>
        <br />
        <input 
        type="number" 
        id="item_price" 
        name="item_price" 
        required onChange = {(e) => setItemPrice(Number(e.target.value))} 
        value={item_price}
        />
        <br />

        <label htmlFor="item_cal">Calorise:</label>
        <br />
        <input 
        type="number" 
        id="item_cal" 
        name="item_cal" 
        required onChange = {(e) => setItemCal(Number(e.target.value))}
        value={item_cal}
        />
        <br /> 
        <input type="submit" value="submit"/>
        </form>
    </div>
    );
}
export default Home