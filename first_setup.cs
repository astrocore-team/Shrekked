Process process = new Process();
process.StartInfo.FileName = "msiexec";
process.StartInfo.WorkingDirectory = @"C:\temp\";
process.StartInfo.Arguments = " /qn+ python3.9.7.msi";
process.StartInfo.Verb = "runas";
process.Start();
process.WaitForExit(60000);