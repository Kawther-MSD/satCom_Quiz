import streamlit as st
import random

st.set_page_config(page_title="🛰️ Iridium - Thuraya - Starlink Support Engineer Quiz Game", layout="centered")

st.title("🛰️ Iridium - Thuraya - Starlink Support Engineer Quiz Game")
st.markdown("Test your knowledge across Land Voice, Data, IoT, and Maritime Iridium - Thuraya - Starlink systems!")

questions = [
 {
        "question": "Which Iridium device supports Push-to-Talk (PTT) functionality?",
        "options": ["Iridium 9555", "Iridium Extreme PTT", "Iridium GO!", "Thales VesseLINK 700"],
        "answer": "Iridium Extreme PTT",
        
        "category": "Land Voice - Iridium",
        "explanation": "Iridium Extreme PTT is designed with Push-to-Talk (PTT) capability for instant group communication."
    },
    {
        "question": "What is the data speed range of the Iridium GO! exec?",
        "options": ["Up to 128 kbps", "22–88 kbps", "~2.4 kbps", "Up to 704 kbps"],
        "answer": "22–88 kbps",
        "category": "Land Data - Iridium",
        "explanation": "Iridium GO! exec supports data speeds from 22 to 88 kbps, suitable for various communication needs."
    },
    {
        "question": "Which Iridium terminal is certified for GMDSS use?",
        "options": ["Iridium 9575", "Iridium GO!", "LT-3100S", "Thales MissionLINK 700"],
        "answer": "LT-3100S",
        "category": "Maritime - Iridium",
        "explanation": "The LT-3100S is IMO-certified for GMDSS maritime safety communications."
    },
    {
        "question": "What is the main connectivity interface of the Iridium Edge IoT device?",
        "options": ["Wi-Fi", "USB-C", "RS-232, TTL", "Ethernet"],
        "answer": "RS-232, TTL",
        "category": "IoT - Iridium",
        "explanation": "Iridium Edge IoT device primarily uses RS-232 and TTL interfaces for connectivity."
    },
    {
        "question": "Which device is best suited for low-bandwidth emergency email and weather in remote zones?",
        "options": ["Iridium 9555", "Iridium GO!", "Iridium GO! exec", "Cobham Explorer 323"],
        "answer": "Iridium GO!",
        "category": "Land Data - Iridium",
        "explanation": "Iridium GO! is optimized for low-bandwidth data like emergency emails and weather info."
    },
    {
        "question": "What are key features of the Iridium Extreme (9575)?",
        "options": ["Dual VoIP, touchscreen, LTE fallback", "SOS button, GPS tracking, AES encryption", "SCADA support, BLE, OTA updates", "Group communications over PTT"],
        "answer": "SOS button, GPS tracking, AES encryption",
        "category": "Land Voice - Iridium",
        "explanation": "Iridium Extreme offers SOS button, GPS tracking, and AES encryption for secure communication."
    },
    {
        "question": "Which devices provide Certus 700-class data speeds (up to 704 kbps)?",
        "options": ["Iridium GO!", "Thales VesseLINK 700 and MissionLINK 700", "Iridium 9555 and Extreme", "LT-3100S and OpenPort"],
        "answer": "Thales VesseLINK 700 and MissionLINK 700",
        "category": "Maritime - Iridium",
        "explanation": "Thales VesseLINK 700 and MissionLINK 700 terminals support Certus 700 speeds up to 704 kbps."
    },
    {
        "question": "Which Iridium device is solar-powered and suitable for long-term asset tracking?",
        "options": ["Iridium Edge", "Iridium Edge Solar", "Iridium GO! exec", "Thales Explorer 323"],
        "answer": "Iridium Edge Solar",
        "category": "IoT - Iridium",
        "explanation": "Iridium Edge Solar is solar-powered, ideal for long-term asset tracking without frequent battery changes."
    },
    {
        "question": "Which Thuraya phone offers dual-mode satellite and GSM connectivity?",
        "options": ["Thuraya XT-PRO DUAL", "Thuraya XT-LITE", "Thuraya SatSleeve", "Thuraya MarineStar"],
        "answer": "Thuraya XT-PRO DUAL",
        "category": "Land Voice - Thuraya",
        "explanation": "Thuraya XT-PRO DUAL is the first dual-mode satellite and GSM phone for seamless connectivity."
    },
    {
        "question": "What is the maximum data speed of the Thuraya IP+ terminal?",
        "options": ["144 kbps", "444 kbps", "100 kbps", "1 Mbps"],
        "answer": "444 kbps",
        "category": "Land Data - Thuraya",
        "explanation": "Thuraya IP+ delivers up to 444 kbps on a shared channel connection."
    },
    {
        "question": "Which Thuraya maritime solution is designed for voice and low-rate data?",
        "options": ["Thuraya MarineStar", "Thuraya Orion IP", "Thuraya XT-PRO", "Thuraya IP Voyager"],
        "answer": "Thuraya MarineStar",
        "category": "Maritime - Thuraya",
        "explanation": "Thuraya MarineStar is ideal for voice and basic data on small to mid-sized vessels."
    },
    {
        "question": "Which Starlink solution is optimized for enterprise-grade connectivity in remote locations?",
        "options": ["Starlink Standard", "Starlink Residential", "Starlink Business", "Starlink RV"],
        "answer": "Starlink Business",
        "category": "Enterprise - Starlink",
        "explanation": "Starlink Business offers high-performance internet for remote work sites and businesses."
    },
    {
        "question": "Which Starlink hardware is best for mobile maritime use?",
        "options": ["Flat High Performance Kit", "Standard Kit", "Premium Kit", "Residential Kit"],
        "answer": "Flat High Performance Kit",
        "category": "Maritime - Starlink",
        "explanation": "The Flat High Performance Kit is designed for in-motion use at sea with high reliability."
    },
    {
        "question": "Which Thuraya phone includes GPS, BeiDou, and Glonass navigation systems?",
        "options": ["Thuraya XT-LITE", "Thuraya XT-PRO", "Thuraya SatSleeve+", "Thuraya MarineStar"],
        "answer": "Thuraya XT-PRO",
        "category": "Land Voice - Thuraya",
        "explanation": "The Thuraya XT-PRO supports advanced GNSS (GPS, BeiDou, Glonass) for location services in remote areas."
    },
    {
        "question": "Which Thuraya device provides circuit-switched voice and SMS via L-band for maritime users?",
        "options": ["Thuraya MarineStar", "Thuraya XT-LITE", "Thuraya SatSleeve Hotspot", "Thuraya Orion IP"],
        "answer": "Thuraya MarineStar",
        "category": "Maritime - Thuraya",
        "explanation": "Thuraya MarineStar is a cost-effective voice/SMS solution for fishing and merchant vessels."
    },
    {
        "question": "What is the maximum data rate of Thuraya Orion IP terminal?",
        "options": ["284 kbps", "444 kbps", "1 Mbps", "128 kbps"],
        "answer": "444 kbps",
        "category": "Maritime Data - Thuraya",
        "explanation": "Thuraya Orion IP provides broadband maritime connectivity up to 444 kbps for voice and data."
    },
    {
        "question": "Which Thuraya solution allows you to use your smartphone via satellite?",
        "options": ["Thuraya XT-PRO DUAL", "Thuraya WE", "Thuraya SatSleeve+", "Thuraya IP+ Hotspot"],
        "answer": "Thuraya SatSleeve+",
        "category": "Land Voice - Thuraya",
        "explanation": "Thuraya SatSleeve+ lets you connect your smartphone to the satellite network for calls and SMS."
    },
    {
        "question": "Which Starlink solution is designed for high-bandwidth enterprise needs with multiple users?",
        "options": ["Starlink Residential", "Starlink Roam", "Starlink Business", "Starlink Mini"],
        "answer": "Starlink Business",
        "category": "Enterprise - Starlink",
        "explanation": "Starlink Business supports higher throughput, fixed IP, and higher reliability for enterprise users."
    },
    {
        "question": "What is the power consumption of Starlink Business terminal (approx.)?",
        "options": ["50W", "100W", "150W", "250W"],
        "answer": "150W",
        "category": "Enterprise - Starlink",
        "explanation": "Starlink Business uses approx. 150W, so backup power planning is important for remote deployment."
    },
    {
        "question": "Which LED status indicates the Starlink dish is booting or searching for signal?",
        "options": ["Blue solid", "White pulsing", "Red blinking", "No light"],
        "answer": "White pulsing",
        "category": "Troubleshooting - Starlink",
        "explanation": "A white pulsing light indicates the dish is booting or seeking a satellite signal."
    },
    {
        "question": "What does a red solid LED on a Starlink router indicate?",
        "options": ["All OK", "Overheating", "No internet connection", "Firmware updating"],
        "answer": "No internet connection",
        "category": "Troubleshooting - Starlink",
        "explanation": "A red LED means the router is unable to connect to the internet via the satellite link."
    },
    {
        "question": "Which issue can be resolved by factory reset on Iridium GO! device?",
        "options": ["Broken antenna", "No GPS lock", "App won't connect", "SIM not detected"],
        "answer": "App won't connect",
        "category": "Troubleshooting - Iridium",
        "explanation": "When the Iridium GO! app fails to connect, factory resetting the device often helps re-pairing."
    },
    {
        "question": "How do you troubleshoot a 'SIM Not Ready' message on Iridium 9555?",
        "options": ["Update firmware", "Reboot device", "Clean SIM contacts and reinsert", "Change antenna"],
        "answer": "Clean SIM contacts and reinsert",
        "category": "Troubleshooting - Iridium",
        "explanation": "A common fix for 'SIM Not Ready' error is to gently clean and reinsert the SIM properly."
    },
    {
        "question": "If a Thuraya XT-LITE displays 'No Network', what's a first step?",
        "options": ["Switch SIM card", "Go outside for clear view of sky", "Reset GPS settings", "Format device"],
        "answer": "Go outside for clear view of sky",
        "category": "Troubleshooting - Thuraya",
        "explanation": "Thuraya devices need direct line of sight to the satellite; go outdoors with sky visibility."
    },
    {
        "question": "What frequency band does the Iridium satellite network use for communication?",
        "options": ["L-band", "Ka-band", "Ku-band", "S-band"],
        "answer": "L-band",
        "category": "Network - Iridium",
        "explanation": "Iridium exclusively operates in the L-band, known for its reliability in all weather conditions and global coverage."
    },
    {
        "question": "Thuraya uses which primary frequency band for its satellite communications?",
        "options": ["C-band", "L-band", "Ka-band", "X-band"],
        "answer": "L-band",
        "category": "Land Data - Thuraya",
        "explanation": "Thuraya primarily operates in the L-band for mobile satellite services due to its robustness and low latency."
    },
    {
        "question": "Which frequency band is primarily used by Starlink to deliver high-speed internet?",
        "options": ["Ku-band and Ka-band", "L-band only", "C-band", "S-band"],
        "answer": "Ku-band and Ka-band",
        "category": "Enterprise - Starlink",
        "explanation": "Starlink uses a combination of Ku-band and Ka-band for higher throughput and performance in satellite broadband services."
    },
    {
        "question": "In Thuraya Maritime systems, which issue could result from poor signal in bad weather?",
        "options": ["Ka-band signal attenuation", "L-band robustness", "No SIM detected", "High-speed fallback"],
        "answer": "Ka-band signal attenuation",
        "category": "Troubleshooting - Thuraya",
        "explanation": "While Thuraya primarily uses L-band, if Ka-band is involved in hybrid terminals, bad weather can attenuate signal due to its higher frequency."
    },
    {
        "question": "Why might Starlink users experience signal dropouts during heavy rain?",
        "options": ["L-band absorption", "Ka-band rain fade", "GPS desynchronization", "Wi-Fi congestion"],
        "answer": "Ka-band rain fade",
        "category": "Troubleshooting - Starlink",
        "explanation": "Ka-band is susceptible to 'rain fade', where moisture in the atmosphere absorbs or scatters signals, affecting connectivity."
    },
    {
        "question": "Why is L-band preferred for Iridium voice services?",
        "options": ["It supports higher frequencies", "L-band is immune to rain fade", "It allows dual SIM cards", "It uses fiber optics"],
        "answer": "L-band is immune to rain fade",
        "category": "Troubleshooting - Iridium",
        "explanation": "L-band is preferred for mobile voice because it maintains signal quality in all weather conditions, unlike Ka-band or Ku-band."
    },
    {
        "question": "Which Starlink antenna model is optimized for high-performance use and features a motorized phased-array design?",
        "options": ["Standard Dish", "Flat High Performance", "Starlink Mini", "Business Kit V1"],
        "answer": "Flat High Performance",
        "category": "Enterprise - Starlink",
        "explanation": "The Flat High Performance antenna is designed for mobility and enterprise, offering better heat resistance and GNSS precision tracking."
    },
    {
        "question": "Which of the following Starlink kits includes Power over Ethernet (PoE) support for connecting external devices?",
        "options": ["Residential Kit", "Starlink Mini", "Flat High Performance Kit", "Standard Gen 3 Kit"],
        "answer": "Flat High Performance Kit",
        "category": "Enterprise - Starlink",
        "explanation": "Only the Flat High Performance Kit includes an Ethernet adapter and supports PoE, a key feature for enterprise integrations."
    },
    {
        "question": "What is a recommended first troubleshooting step when the Starlink dish shows 'Searching' for over 20 minutes?",
        "options": ["Factory reset the router", "Wait for firmware update", "Verify dish has clear sky view", "Switch to mobile data"],
        "answer": "Verify dish has clear sky view",
        "category": "Troubleshooting - Starlink",
        "explanation": "The Starlink dish needs a wide, unobstructed view of the sky to connect to satellites. Obstructions like trees or walls are the main cause of prolonged 'Searching' status."
    },
    {
        "question": "Which light status on the Starlink router indicates a possible Ethernet backhaul connection failure?",
        "options": ["No light", "Blue light", "White light", "Flashing amber"],
        "answer": "No light",
        "category": "Troubleshooting - Starlink",
        "explanation": "If the LED is off and there's no internet, it may indicate a hardware fault or disconnected Ethernet backhaul, especially in wired setups."
    },
    {
        "question": "What tool is recommended for identifying obstructions and optimizing dish placement?",
        "options": ["Speedtest.net", "Dishpointer.com", "Starlink App – Obstruction Scan", "GPS Compass"],
        "answer": "Starlink App – Obstruction Scan",
        "category": "Troubleshooting - Starlink",
        "explanation": "The official Starlink app has a built-in Obstruction Scan tool that uses augmented reality to check for signal blockages around the dish."
    },
    {
        "question": "Which issue may occur if the Starlink dish cable is extended with a non-certified third-party cable?",
        "options": ["Overheating of dish", "Weak Wi-Fi signal", "Power delivery issues", "Excessive data usage"],
        "answer": "Power delivery issues",
        "category": "Troubleshooting - Starlink",
        "explanation": "Starlink dishes require a specific voltage. Using third-party cables can cause voltage drop, resulting in boot loops or connection failures."
    },
    {
        "question": "Which Starlink feature allows seamless failover between multiple internet sources (e.g., Starlink + LTE)?",
        "options": ["Load Balancer", "Multi-WAN Fusion", "Failover DNS", "Ethernet Adapter"],
        "answer": "Multi-WAN Fusion",
        "category": "Enterprise - Starlink",
        "explanation": "Starlink Business users can configure multi-WAN failover with compatible enterprise routers to ensure redundancy."
    },
    {
        "question": "What is the expected average latency of Starlink in optimal conditions?",
        "options": ["<20 ms", "50–70 ms", "100–150 ms", "200–300 ms"],
        "answer": "50–70 ms",
        "category": "Enterprise - Starlink",
        "explanation": "While Starlink aims for <20 ms with inter-satellite laser links, average latencies for most users are around 50–70 ms."
    },
    {
        "question": "How can a user identify whether their Starlink system is thermal throttling due to heat?",
        "options": ["Check LED color", "Listen for fan noise", "Monitor 'Thermal Shutdown' warning in app", "Check router placement"],
        "answer": "Monitor 'Thermal Shutdown' warning in app",
        "category": "Troubleshooting - Starlink",
        "explanation": "The Starlink app displays thermal alerts and error logs if the dish or router overheats, which can reduce performance or cause reboots."
    },
    {
        "question": "What does 'DC over coax' mean in the context of Starlink hardware?",
        "options": ["Dual-channel output via coax", "Data compression via coax", "Power and data transmitted over same coax cable", "Data conversion for local caching"],
        "answer": "Power and data transmitted over same coax cable",
        "category": "Enterprise - Starlink",
        "explanation": "Starlink hardware uses DC over coax to power the dish and transmit data simultaneously, simplifying installation and reducing cable requirements."
    },
    {
        "question": "What could cause an 'Invalid SIM' error on an Iridium 9575 phone after SIM insertion?",
        "options": ["Outdated firmware", "Incorrect APN settings", "SIM inserted upside-down", "Corrupted contacts"],
        "answer": "SIM inserted upside-down",
        "category": "Troubleshooting - Iridium",
        "explanation": "The Iridium 9575 requires the SIM to be inserted in a precise orientation. Inserting it incorrectly can trigger a SIM error."
    },
    {
        "question": "After inserting a new SIM into a Thuraya XT-PRO, the user sees 'No Network'. What is the likely cause?",
        "options": ["SIM is not activated", "Device is in airplane mode", "Antenna disconnected", "Dust in SIM slot"],
        "answer": "SIM is not activated",
        "category": "Troubleshooting - Thuraya",
        "explanation": "New Thuraya SIMs must be activated by the provider before the device can register on the network."
    },
    {
        "question": "A user moves their Starlink terminal to a new country and cannot connect. What's the likely cause?",
        "options": ["Incorrect firmware", "Region lock on account", "VPN conflict", "Router overheating"],
        "answer": "Region lock on account",
        "category": "Troubleshooting - Starlink",
        "explanation": "Starlink is geo-locked per service plan. Moving to another country requires requesting relocation or a mobility plan."
    },
    {
        "question": "An Iridium GO! device is connected, but cannot make calls or send messages. What might be missing?",
        "options": ["Antenna firmware", "Voice + data provisioning", "Wi-Fi calibration", "Satellite sync time"],
        "answer": "Voice + data provisioning",
        "category": "Troubleshooting - Iridium",
        "explanation": "Iridium devices must be correctly provisioned (voice/data/SBD) through the provider for services to work."
    },
    {
        "question": "A Thuraya device shows a strong signal but cannot register to the network. What might be the cause?",
        "options": ["SIM is region-restricted", "SIM has expired", "Low battery", "Outdated timezone"],
        "answer": "SIM is region-restricted",
        "category": "Troubleshooting - Thuraya",
        "explanation": "Some Thuraya SIMs are tied to specific regions. Using them outside their coverage zone can prevent registration."
    },
    {
        "question": "A business user receives a 'Device not authorized' message after hardware swap. Likely cause?",
        "options": ["SIM not inserted", "MAC address not whitelisted", "Incorrect voltage", "Obstructed view"],
        "answer": "MAC address not whitelisted",
        "category": "Troubleshooting - Starlink",
        "explanation": "Starlink authorizes terminals based on serial/MAC. If the hardware is changed without account sync, service is denied."
    },
    {
        "question": "An Iridium Edge is connected but fails to send SBD messages. What should be verified first?",
        "options": ["Check GPS lock", "Check battery level", "Check VoIP profile", "Reboot router"],
        "answer": "Check GPS lock",
        "category": "Troubleshooting - Iridium",
        "explanation": "Iridium SBD messages require a valid GPS fix. No lock will cause failed message transmission."
    },
    {
        "question": "The Thuraya XT-LITE displays 'Insert SIM' even though one is inserted. What could help?",
        "options": ["Enable roaming", "Wipe contacts", "Clean SIM tray", "Change language"],
        "answer": "Clean SIM tray",
        "category": "Troubleshooting - Thuraya",
        "explanation": "Dust or misalignment can prevent SIM detection. Cleaning and reinserting often solves the issue."
    },
    {
        "question": "A user requests relocation of Starlink service but sees 'Pending Location Update' for hours. What is required?",
        "options": ["Manual restart", "Wi-Fi name reset", "GPS fix confirmation", "Wait for Starlink approval"],
        "answer": "Wait for Starlink approval",
        "category": "Troubleshooting - Starlink",
        "explanation": "Relocation requires backend authorization, which can take a few hours to fully update across the satellite system."
    },
    {
        "question": "A SIM is moved from one Iridium GO! device to another and fails to connect. What may be required?",
        "options": ["Full reset", "Satellite pass check", "APN reconfiguration", "Reprovisioning the new IMEI"],
        "answer": "Reprovisioning the new IMEI",
        "category": "Troubleshooting - Iridium",
        "explanation": "Some Iridium services are linked to both SIM and device IMEI. Swapping requires reprovisioning or carrier sync."
    },




]

def initialize_quiz():
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.category_scores = {}
    st.session_state.answered = {}
    st.session_state.show_explanation = False
    st.session_state.quiz_complete = False
    st.session_state.selected_answer = None
    # Initialize category scores with zeros
    for q in st.session_state.shuffled_questions:
        cat = q["category"]
        if cat not in st.session_state.category_scores:
            st.session_state.category_scores[cat] = {"correct": 0, "total": 0}
        st.session_state.category_scores[cat]["total"] += 1

if "shuffled_questions" not in st.session_state:
    initialize_quiz()

def show_question():
    q_index = st.session_state.q_index
    question = st.session_state.shuffled_questions[q_index]
    cat = question["category"]

    st.write(f"❓ Question {q_index + 1} of {len(st.session_state.shuffled_questions)}")
    st.write(f"Category: **{cat}**")
    st.write(f"### {question['question']}")

    # Use a unique key for the radio button
    user_choice = st.radio(
        "👉 Choose an answer:", 
        question["options"], 
        key=f"radio_{q_index}"
    )

    # Store the selected answer
    st.session_state.selected_answer = user_choice

    # Submit button logic
    if not st.session_state.answered.get(q_index, False):
        if st.button("Submit Answer", key=f"submit_{q_index}"):
            st.session_state.answered[q_index] = True
            st.session_state.show_explanation = True
            correct_answer = question["answer"]

            if user_choice == correct_answer:
                st.session_state.score += 1
                st.session_state.category_scores[cat]["correct"] += 1
            
            st.rerun()
    else:
        # Show answer feedback
        correct_answer = question["answer"]
        if st.session_state.selected_answer == correct_answer:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. Correct answer: **{correct_answer}**")

        if st.session_state.show_explanation:
            st.info(f"📘 Explanation: {question['explanation']}")

        # Next question button
        if q_index < len(st.session_state.shuffled_questions) - 1:
            if st.button("Next Question", key=f"next_{q_index}"):
                st.session_state.q_index += 1
                st.session_state.show_explanation = False
                st.session_state.selected_answer = None
                st.rerun()
        else:
            st.success("🎉 This was the last question! Submit the quiz to see your results.")
            if st.button("See Results", key="see_results"):
                st.session_state.quiz_complete = True
                st.rerun()

def show_results():
    st.write("### 🎉 Quiz Complete!")
    st.write(f"Your total score is **{st.session_state.score}** out of **{len(st.session_state.shuffled_questions)}**.")

    st.write("### Scores by Category:")
    for cat, scores in st.session_state.category_scores.items():
        st.write(f"- {cat}: {scores['correct']} / {scores['total']}")

    if st.session_state.score >= len(st.session_state.shuffled_questions) * 0.8:
        st.balloons()
        st.success("🚀 Expert Level – You're ready for advanced support roles!")
    elif st.session_state.score >= len(st.session_state.shuffled_questions) * 0.5:
        st.info("✅ Well Done – Just review a few more devices.")
    else:
        st.warning("⚠️ Needs Review – Focus on key specs and use cases.")

    if st.button("Restart Quiz", key="restart_quiz"):
        initialize_quiz()
        st.rerun()

if not st.session_state.quiz_complete:
    show_question()
else:
    show_results()