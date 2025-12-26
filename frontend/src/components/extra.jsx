function Home() {
    // Change state variable names to match your model
    const [item_name, setItemName] = useState("");
    const [item_desc, setItemDesc] = useState("");
    const [item_price, setItemPrice] = useState(0);
    const [item_cal, setItemCal] = useState(0);
    
    // In your form, update the inputs:
    return (
        <div>
            <form onSubmit={createItem}>
                <label htmlFor="item_name">Item Name:</label>
                <input 
                    type="text" 
                    id="item_name" 
                    name="item_name" 
                    required 
                    onChange={(e) => setItemName(e.target.value)} 
                    value={item_name}
                />
                
                <label htmlFor="item_desc">Item Description:</label>
                <textarea 
                    name="item_desc" 
                    id="item_desc" 
                    required 
                    value={item_desc} 
                    onChange={(e) => setItemDesc(e.target.value)}
                />
                
                <label htmlFor="item_price">Price:</label>
                <input 
                    type="number" 
                    id="item_price" 
                    name="item_price" 
                    required 
                    onChange={(e) => setItemPrice(e.target.value)} 
                    value={item_price}
                />
                
                <label htmlFor="item_cal">Calories:</label>
                <input 
                    type="number" 
                    id="item_cal" 
                    name="item_cal" 
                    onChange={(e) => setItemCal(e.target.value)} 
                    value={item_cal}
                />
                
                <input type="submit" value="Submit"/>
            </form>
        </div>
    );
    
    // Update your createItem function:
    const createItem = (e) => {
        e.preventDefault();
        api.post("/api/notes/", {
            item_name,
            item_desc,
            item_price,
            item_cal
        }).then((res) => {
            if (res.status === 201) alert("Item was created successfully");
            else alert("Failed to create an Item");
        }).catch((error) => alert(error));
        getItems();
    };
}