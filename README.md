# PassioGo_MCP_Server

An intelligent backend service for interacting with real-time transportation data from PassioGO systems. Built with FastMCP.

---

## Author/Contact Information
Name: Jozef Dusenka
email: dusenka.jozef@gmail.com

## Instructions to run on Claude Desktop
- This MCP server can be run on any other MCP client; however, the instructions to run might differ slightly.
- Download Claude Desktop ((https://claude.ai/download))
- Download this repository.
- Open Claude Dektop -> File -> Settings -> Developer -> Edit Config
- Open claude_desktop_config.json file
- If empty, replace with:
```json
{
    "mcpServers": {
        "passioGo": {
            "command": "uv",
            "args": [
                "--directory",
                "C:\\Path to the \\PassioGo_MCP_Server",
                "run",
                "main.py"
            ]
        }
    }
}
```
- Save changes and restart Claude Desktop
- Claude Desktop now should include the avaliable Passio Go MCP server tools but showing a small hammer icon
- MCP client then automatically desides if any of the tools are needed to answer the question

## Example
###User:
I'm at the union station at the University of Arkansas. What busses are stopping here in the next 5 minutes?
I would like to go north to the agricultural part of the campus. What busses can I take?

---

###Claude Desktop:
I'll help you find out which buses are stopping at Union Station at the University of Arkansas in the next few minutes. Let me check the transportation system information.

Now I'll check for the active vehicles that will be arriving at Union Station soon:

Now I'll check if there are any alerts for the transportation system:

Based on the information I've gathered, here are the buses that should be arriving at Union Station within the next 5 minutes:

Route 26 Peak (Red Bus #27) - Currently at or very near the Union Station stop
Route 21 Peak (Blue Bus #43) - Currently near Union Station
Route 48 Peak (Pink Bus #32) - Currently near Union Station

Please note there's an active alert that the Passio live map is experiencing some issues today, which may affect the accuracy of real-time arrival predictions. The transportation system is called Razorback Transit at the University of Arkansas.
Since bus #27, #43, and #32 appear to be very close to or at Union Station based on their coordinates, these are your best options within the next 5 minutes. If you need to go to a specific destination, let me know and I can help determine which route would be best for you.

---

###User:
I would like to go north to the agricultural part of the campus. What busses can I take?

---

I'll help you find buses that go north to the agricultural part of campus from Union Station.
Let me check which routes from Union Station head to the northern agricultural areas of the University of Arkansas campus.

Based on the information I've gathered, here are your best options to get from Union Station to the agricultural part of the University of Arkansas campus (which is located in the northern area of campus):
Best Option: Route 21 Peak (Blue Bus)
This route goes directly to the agricultural areas with stops at:

Food Science (north campus)
Crafton Place (agricultural area)
Garland & Sycamore
Fair Park

The Route 21 Peak bus (#43) is currently en route to Union Station and would be an excellent choice for reaching the agricultural part of campus.
Alternative Option: Route 26 Peak (Red Bus)
This route also heads north from Union Station with stops at:

Plant Science
South Creekside
And continues further north to various locations

The Route 26 Peak bus (#27) is currently near Union Station.
Other Option: Route 33 Peak (Orange Bus)
While this route goes north, it heads more northwest rather than directly to the agricultural areas. It may not be the most direct route to the agricultural part of campus.
I recommend taking the Route 21 Peak (Blue) bus as it appears to most directly serve the agricultural areas with stops at Food Science and other agriculture-related locations in the northern part of campus.

