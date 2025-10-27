import asyncio
import json

# Store active WebSocket connections
active_connections = set()


async def websocket_application(scope, receive, send):
    """Handle WebSocket connections for real-time notifications."""
    # Accept the connection
    await send({"type": "websocket.accept"})
    
    # Add this connection to active connections
    connection = {"receive": receive, "send": send}
    active_connections.add(id(connection))
    
    try:
        while True:
            event = await receive()

            if event["type"] == "websocket.disconnect":
                break

            if event["type"] == "websocket.receive":
                # Handle ping-pong for connection testing
                if event.get("text") == "ping":
                    await send({"type": "websocket.send", "text": "pong!"})
    finally:
        # Remove connection when it closes
        active_connections.discard(id(connection))


async def broadcast_notification(notification_html):
    """Broadcast a notification to all connected WebSocket clients."""
    # Create a list of tasks to send to all connections
    # Note: This is a simplified implementation
    # In production, you'd want a more robust connection management system
    pass  # Actual broadcasting will be handled by the view using Django Channels or similar
