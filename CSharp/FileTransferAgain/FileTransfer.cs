using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace FileTransferCSharp
{
    public class TransferFiles
    {
        string sourcePath = @"C:\Users\Public\Folder1\";
        string destPath = @"C:\Users\Public\Folder2\";

        static void Main(string[] args)
        {
            TransferFiles t = new TransferFiles();

            if (!Directory.Exists(t.destPath))
            {
                Directory.CreateDirectory(t.destPath);
            }

            if (Directory.Exists(t.sourcePath))
            {
                string filext = "*";
                string[] files = Directory.GetFiles(t.sourcePath, filext);
                Console.WriteLine(files);

                // Copy the files less than 24hrs old, overwrites existing files
                foreach (string s in files)
                {
                    DateTime fileDate = File.GetLastWriteTime(s);
                    Console.WriteLine(fileDate);
                    bool timeCheck = fileDate > DateTime.Now.AddHours(-24);
                    Console.WriteLine(timeCheck);

                    if (timeCheck == true)
                    {
                        t.sourcePath = Path.GetFileName(s);
                        Console.WriteLine(t.sourcePath);
                        File.Copy(s, Path.Combine(t.destPath,Path.GetFileName(s)));
                        Console.WriteLine("Transferring file ... ");
                    }
                }
                Console.WriteLine("\nFile transfer complete.\n");
            }
            else
            {
                Console.WriteLine("Source path does not exist.");
            }
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();

        }
    }
}
