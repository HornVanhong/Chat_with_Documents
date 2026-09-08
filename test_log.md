# RAG System Evaluation Test Log (Step 7)

This test log documents the execution of the 5 required benchmark questions.

- **Embedding Model**: `nomic-embed-text` (Ollama)
- **LLM Generation Model**: `llama3.2` (Ollama)
- **Vector Database**: `ChromaDB` (Persistent, Cosine Distance)

---

## Test #1: In-Document (PIN Reset)
**Question**: `How do I reset my forgotten PIN on a company device, and what happens if I fail too many times?`

**Confidence Gate Passed**: `True` (Best Cosine Distance: `0.1333`)

### Retrieved Chunks:
1. **[002_Resetting_a_Forgotten_PIN.txt]** (distance = `0.1333`):
   > "o reset your PIN.  By following these steps, you should be able to reset your forgotten PIN and regain access to company systems and applications. If you encounter any issues durin..."

2. **[002_Resetting_a_Forgotten_PIN.txt]** (distance = `0.1459`):
   > "**Resetting a Forgotten PIN**  If you have forgotten your PIN, you can reset it using the following steps:  **Step 1: Access the PIN Reset Tool**  1. Go to the company's intranet h..."

3. **[002_Resetting_a_Forgotten_PIN.txt]** (distance = `0.1719`):
   > "2. Click the "OK" button to close the message.  **Important Notes:**  * If you are unable to reset your PIN using the self-service tool, please contact the IT Helpdesk for assistan..."

### Generated Answer:
To reset your forgotten PIN on a company device, follow these steps:

1. Go to the company's intranet homepage and click on the "IT Support" link at the top right corner of the page.
2. Click on the "Self-Service" tab and then select "PIN Reset" from the drop-down menu.
3. You will be redirected to the PIN Reset Tool login page.
4. Enter your company username and password.
5. Click the "OK" button to close the message.

If you fail to reset your PIN too many times within a 24-hour period, you will need to contact the IT Helpdesk for assistance.

---

## Test #2: In-Document (VPN Setup)
**Question**: `What are the prerequisites and steps to configure VPN access for remote workers?`

**Confidence Gate Passed**: `True` (Best Cosine Distance: `0.0760`)

### Retrieved Chunks:
1. **[003_Configuring_VPN_Access_for_Remote_Workers.txt]** (distance = `0.0760`):
   > "**Configuring VPN Access for Remote Workers**  **Overview**  This article provides step-by-step instructions for configuring VPN access for remote workers. This allows employees wo..."

2. **[003_Configuring_VPN_Access_for_Remote_Workers.txt]** (distance = `0.1380`):
   > "em requirements for VPN connectivity. * The remote worker must have a valid company login credentials. * The remote worker must have a stable internet connection.  **Step 1: Instal..."

3. **[003_Configuring_VPN_Access_for_Remote_Workers.txt]** (distance = `0.2263`):
   > "these steps, remote workers can securely connect to the company network and access company resources from anywhere. If you have any questions or issues, please contact the IT helpd..."

### Generated Answer:
According to the provided context, the prerequisites for configuring VPN access for remote workers are:

1. The remote worker's device (laptop or desktop) must meet the company's minimum system requirements for VPN connectivity.
2. The remote worker must have a valid company login credential.
3. The remote worker must have a stable internet connection.

The steps to configure VPN access for remote workers are:

1. Install the VPN client software by:
   - Going to the company's software portal and downloading the VPN client software.
   - Running the installer and following the prompts to install the software.
   - Launching the VPN client software.

2. Configure the VPN connection by:
   - Clicking on "New Connection" in the VPN client software.
   - (Steps not explicitly provided in the context)

---

## Test #3: In-Document (Cisco Webex)
**Question**: `How do I schedule a conference call and invite participants using Cisco Webex?`

**Confidence Gate Passed**: `True` (Best Cosine Distance: `0.0867`)

### Retrieved Chunks:
1. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.0867`):
   > "To set up a conference call on Cisco Webex, follow these steps:  **Step 1: Log in to Cisco Webex**  Open a web browser and navigate to [company Webex URL]. Enter your company login..."

2. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.1724`):
   > "b and select "Cisco Webex Video" as the default video type. You can also choose to allow participants to join via video.  **Step 5: Add Agenda and Notes (Optional)**  You can add a..."

3. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.2290`):
   > "y restarting your browser or checking your internet connection. * If you experience audio or video issues during the meeting, try restarting your audio or video settings or contact..."

### Generated Answer:
To schedule a conference call and invite participants using Cisco Webex, follow these steps:

**Step 1: Log in to Cisco Webex**

Open a web browser and navigate to [company Webex URL]. Enter your company login credentials to access the Webex portal.

**Step 2: Schedule a Meeting**

Click on the "Meetings" tab and select "Schedule a Meeting" from the drop-down menu. Fill in the required information, including:

* Meeting topic
* Start and end time
* Duration
* Invitees (add email addresses or names from the company directory

**Step 3: Add Video Type and Joining Options**

Select "Cisco Webex Video" as the default video type. You can also choose to allow participants to join via video.

**Step 4: Add Agenda and Notes (Optional)**

You can add an agenda and notes to the meeting invitation by clicking on the "Agenda" tab. This information will be visible to all invitees.

**Step 5: Send Invitations**

Click "Schedule" to send the meeting invitation to all invitees. The invitation will include a link to join the meeting, as well as dial-in information for audio.

By following these steps, you can successfully schedule a conference call and invite participants using Cisco Webex.

---

## Test #4: Out-of-Document (Hallucination Test)
**Question**: `What is the recipe and baking temperature for chocolate fudge brownies?`

**Confidence Gate Passed**: `False` (Best Cosine Distance: `0.5735`)

### Retrieved Chunks:
1. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.5735`):
   > "* Start and end time * Duration * Invitees (add email addresses or names from the company directory)  **Step 3: Configure Audio Settings**  In the "Audio" section, select "Cisco We..."

2. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.5811`):
   > "b and select "Cisco Webex Video" as the default video type. You can also choose to allow participants to join via video.  **Step 5: Add Agenda and Notes (Optional)**  You can add a..."

3. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.5926`):
   > "and video settings before the meeting to ensure a smooth experience. * Encourage invitees to join the meeting 5-10 minutes early to troubleshoot any technical issues. * Use the "Mu..."

### Generated Answer:
I could not find this in your documents.

---

## Test #5: Out-of-Document / Edge Case (Non-IT Policy)
**Question**: `How do I request a reimbursement for an international airline ticket?`

**Confidence Gate Passed**: `False` (Best Cosine Distance: `0.4900`)

### Retrieved Chunks:
1. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.4900`):
   > "b and select "Cisco Webex Video" as the default video type. You can also choose to allow participants to join via video.  **Step 5: Add Agenda and Notes (Optional)**  You can add a..."

2. **[005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt]** (distance = `0.5117`):
   > "To set up a conference call on Cisco Webex, follow these steps:  **Step 1: Log in to Cisco Webex**  Open a web browser and navigate to [company Webex URL]. Enter your company login..."

3. **[003_Configuring_VPN_Access_for_Remote_Workers.txt]** (distance = `0.5140`):
   > "em requirements for VPN connectivity. * The remote worker must have a valid company login credentials. * The remote worker must have a stable internet connection.  **Step 1: Instal..."

### Generated Answer:
I could not find this in your documents.

---
