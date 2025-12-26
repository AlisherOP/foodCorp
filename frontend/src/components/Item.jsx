
import React from "react";
import  "../styles/Item.css"
function Item({item, onDelete}){
    // create date
    const formattedDate = new Date(item.created_at).toLocaleDateString("en-US")
    return (<div className="note-container">
        <h1 className="note-title">{item.item_name}</h1>
        <p className="note-container">{item.item_desc}</p>
        <p className="note-container">{item.item_price}$</p>
        <p className="note-container">{item.item_cal}Cal</p>
        <p className="note-date">{formattedDate}</p>
        <button className="delete-button" onClick={() => onDelete(item.id) }>
            Delete
            </button>
    </div>
    );
}
export default Item