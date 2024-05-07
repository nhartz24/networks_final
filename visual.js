// Function to add a new node to the network visualization
function addNode(x, y) {
    // Create a new div element for the node
    const newNode = document.createElement('div');
    newNode.className = 'node';
    
    // Set the position of the node
    newNode.style.left = x + 'px';
    newNode.style.top = y + 'px';
    
    // Append the node to the network container
    document.getElementById('network-container').appendChild(newNode);
}

// Example usage: add a node at position (100, 100)
addNode(100, 100);
