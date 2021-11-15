import * as http from "http";
import { logRobotFramework, clearRobotFrameworkLog } from "./channel";


export class ListenerServer {
    port = 5696;
    server: http.Server;

    constructor() {
        this.server = http.createServer(this.requestListener)
                          .listen(this.port);
    }

    requestListener(request: http.IncomingMessage, response: http.ServerResponse) {
        if (request.method === "POST") {
            if(request.url?.endsWith('clear'))
            {
                clearRobotFrameworkLog();
                response.end();
            }

            if(request.url?.endsWith('log'))
            {
                let data : Uint8Array[] = [];
    
                request.on("data", chunk => {
                    data.push(chunk);
                });
        
                request.on("end", () => {
                    let body = Buffer.concat(data).toString();
                    logRobotFramework(body);
                    response.end();
                });
            }
        }
    }

    stop() {
        this.server.close();
    }
}
