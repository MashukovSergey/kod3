using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;

namespace Krestiki_and_zeriki
{
    class Program
    {
        static void Main(string[] args)
        {
            Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            String a;
            Socket cl;
            byte[] mas = new byte[20];
            a = Console.ReadLine();
            if (a == "s")
            {
                socket.Bind(new System.Net.IPEndPoint(System.Net.IPAddress.Parse("127.0.0.1"), 8888));
                socket.Listen(0);
                cl = socket.Accept();
                String str = "zxzxzxzx";
                
                mas=Encoding.UTF8.GetBytes(str);
                cl.Send(mas);
            }
            else 
            {
                try
                {
                    socket.Connect(new System.Net.IPEndPoint(System.Net.IPAddress.Parse("127.0.0.1"), 8888));
                }
                catch
                {
                    Console.WriteLine("Сервер спит.");
                    return;
                }
                int xcv = socket.Receive(mas);
                string str;
                str=Encoding.UTF8.GetString(mas,0,xcv);
                Console.WriteLine(str);
            }
        }
    }
}
