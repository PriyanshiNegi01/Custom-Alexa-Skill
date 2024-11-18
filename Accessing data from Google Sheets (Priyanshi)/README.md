# Accessing Data from Google Sheets (Priyanshi) - Custom Alexa Skill  
**Skill Invocation Name**: *Google Sheets*

## Project Overview  
This Alexa Skill enables users to interact with a Google Sheet via voice commands. By integrating Alexa with ChatGPT, the skill processes user intents to read, write, or search data in a Google Sheet. Created under German mentorship, this project explores the workings of intents, voice-based response delivery, and mastery of the Alexa Developer Console.

---

## Features  
- **Read Data**: Fetch values from specific cells in a Google Sheet.  
- **Write Data**: Update a cell with user-provided information.  
- **Search Data**: Look up specific entries in the Google Sheet and retrieve relevant results.  
- **Natural Voice Interaction**: Intuitive commands for seamless voice-based interaction.  

---

## Invocation Name  
The skill's invocation name is:  
**"Google Sheets"**  
> Example command: *"Alexa, ask Google Sheets to read cell A1."*

---

## File Structure  

### **1. `lambda/`**  
Contains the core logic and intent handlers for the Alexa Skill.  
- **`handlers/`**:
  - `hello_world_handler.py`: Handles the default "Hello World" intent.
  - `launch_request_handler.py`: Manages the skill's launch requests.
  - `read_cell_intent_handler.py`: Reads data from a specified cell in the Google Sheet.
  - `search_intent_handler.py`: Searches for specific data in the sheet based on keywords.
  - `write_to_cell.py`: Writes user-provided information to the specified cell.  

### **2. `assets/`**  
- **`images/`**: Stores graphical assets for the Alexa Developer Console.
- Other assets, such as configuration files or additional resources.  

### **3. `interactionModels/`**  
- **`custom/`**: Contains JSON files defining the skill’s interaction model, including intents, utterances, and slots.

---

## How It Works  

1. **Skill Invocation**: The user initiates the skill by saying the invocation name followed by a command.  
   Example: *"Alexa, ask Google Sheets to read cell c2."*  

2. **Intent Handling**: Based on the user's request, Alexa routes the command to the appropriate intent handler.  

3. **Google Sheets Integration**: Handlers communicate with the Google Sheets API to perform the requested operations.  

4. **Response Delivery**: Alexa processes the results and responds naturally to the user with relevant information.  

---

## Prerequisites  

### **1. Developer Accounts**  
- **Amazon Developer Account**: To access and deploy the Alexa Skill.  
- **Google Cloud Console**: For setting up APIs and accessing Google Sheets.  

### **2. Tools and Frameworks**  
- Python for Lambda handlers.  
- Alexa Developer Console for skill creation.  

### **3. Configuration**  
- Link Google Sheets with appropriate API credentials in your Lambda functions.  
- Customize intents in `interactionModels/custom`.  

---

## Setup Instructions  

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-repo>.git
   cd custom-alexa-skill-google-sheets
   ```

2. Configure the `lambda` folder:
   - Replace placeholders in the handler scripts (e.g., API keys, Sheet IDs).  

3. Deploy Lambda Functions:
   - Zip the Lambda directory and upload it to the AWS Lambda Console.

4. Configure Interaction Model:
   - Upload JSON files from `interactionModels/custom` to the Alexa Developer Console.  

5. Test the Skill:
   - Use the Alexa Developer Console's simulator or an Alexa-enabled device.  

---

## Future Enhancements  

- **Multi-sheet Support**: Enable switching between multiple Google Sheets.  
- **Advanced Search Queries**: Incorporate complex queries with filters and ranges.  
- **Error Handling**: Improve responses for invalid or unsupported commands.  

---
<!--
## Contributors  
- **Priyanshi Negi**  
  - Role: Intent Design, Data Integration, Report Writing  
- **Mentorship**: German Mentor (Dr. Arman Nassirtoussi)  

--- 
-->
## License  
This project is licensed under the MIT License.  

--- 

Feel free to customize this further based on any additional details you'd like to include!
