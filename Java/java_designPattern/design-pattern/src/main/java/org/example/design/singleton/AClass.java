package org.example.design.singleton;

public class AClass {

    private SocketClient socketClient;

    public AClass() {
        this.socketClient = SocketClient.getInstance();
    }

    public SocketClient getSocketClient() {
        return socketClient;
    }

    public void setSocketClient(SocketClient socketClient){
        this.socketClient = socketClient;
    }
}
