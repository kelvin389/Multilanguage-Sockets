using System;
using System.Text.Json;
using System.Net.Sockets;
using System.Text;

namespace Sender
{
    class Sender
    {
        private const string Host = "127.0.0.1";
        private const int Port = 1234;
        
        static void Main(string[] args)
        {
            TestObject.TestObject obj = new TestObject.TestObject();
            obj.field1 = 12345;
            obj.field2 = "Hello World from C#!";
            string serializedObjStr = JsonSerializer.Serialize(obj);
            byte[] serialzedObj = Encoding.ASCII.GetBytes(serializedObjStr);
            
            // open socket and send serialized object
            Socket sock = new Socket(SocketType.Stream, ProtocolType.Tcp);
            sock.Connect(Host, Port);
            int bytesSent = 0;
            while (bytesSent < serialzedObj.Length)
            {
                bytesSent += sock.Send(serialzedObj);
            }
            sock.Close();
        }
    }
}