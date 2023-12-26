using System;
using System.Net;
using System.Text.Json;
using System.Net.Sockets;
using System.Runtime.InteropServices;
using System.Text;

namespace Receiver
{
    class Receiver
    {
        private const string Host = "127.0.0.1";
        private const int Port = 1234;
        
        static void Main(string[] args)
        {
            IPAddress ipAddress;
            IPAddress.TryParse(Host, out ipAddress);
            IPEndPoint endPoint = new IPEndPoint(ipAddress, Port);
            
            Socket sock = new Socket(SocketType.Stream, ProtocolType.Tcp);
            sock.Bind(endPoint);
            sock.Listen();
            Socket con = sock.Accept();

            byte[] buf = new byte[1024];
            string received = "";
            while (true)
            {
                int numReceived = con.Receive(buf);
                if (numReceived == 0) break;
                received += Encoding.ASCII.GetString(buf, 0, numReceived);
            }
            con.Close();
            sock.Close();

            Console.Out.Write(received);
            TestObject.TestObject obj = JsonSerializer.Deserialize<TestObject.TestObject>(received);
        }
    }
}