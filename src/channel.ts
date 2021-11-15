import { window } from "vscode";

export const RF_LOG_CHANNEL = window.createOutputChannel("Robot Framework Log");

export async function clearRobotFrameworkLog() {
    RF_LOG_CHANNEL.clear();
}

export async function logRobotFramework(logEntry: string) {
    RF_LOG_CHANNEL.appendLine(logEntry);
}
