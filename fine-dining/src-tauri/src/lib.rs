use tauri::AppHandle;
use tauri::Emitter;

// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
#[tauri::command]
fn reserve(app: AppHandle, reservation: serde_json::Value) -> String {
    // Convert the reservation to a JSON string
    let json_str = reservation.to_string();
    
    // Create command to run Python script with the JSON data
    let output = std::process::Command::new("python3")
        .arg("src/reserve.py")
        .arg(&json_str)
        .output()
        .expect("Failed to execute Python script");

    // You can handle the Python script output here if needed
    let result = String::from_utf8_lossy(&output.stdout);
    
    app.emit("event_name", "eventpayload").unwrap();
    format!("Reservation Details: {}", result)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![reserve])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
