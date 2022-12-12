package org.example.design.singleton;

public class BClass {

    private SocketClient socketClient;

    public BClass() {
        this.socketClient = SocketClient.getInstance();
    }
    public SocketClient getSocketClient() {
        return socketClient;
    }
    public void setSocketClient(SocketClient socketClient){
        this.socketClient = socketClient;
    }
}
