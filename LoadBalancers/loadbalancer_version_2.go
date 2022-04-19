package main
import "net"
import "log"
import "io"
import "fmt"
import "os"
import "bufio"

var (
        counter int
        modNumber int =3
        listenAddr = "localhost:8080"

        server=[]string{
                "localhost:5001",
                "localhost:5002",
                "localhost:5003",
                "localhost:5004",
                "localhost:5005",
        }
)


func main(){
        listener,err:= net.Listen("tcp", listenAddr)
        if err != nil {
                log.Fatal("Failed to listen %s ")
        }
        defer listener.Close()
        for {
                conn,err:=listener.Accept()

                if err != nil{
                        log.Printf("failed to accept connection %s",err)
                }

                backend:=chooseBackend()
                fmt.Printf("counter=%d baxkend=%s \n",counter,backend)
                go func(){
                        err:=proxy(backend, conn)
                        if err != nil {
                                log.Printf("WARNING : proxying failed %v",err)
                        }
                }()
        }
}

func AppendFile() {
        file, err := os.OpenFile("flag.txt", os.O_WRONLY, 0644)
        if err != nil {
                log.Fatalf("failed opening file: %s", err)
        }
        defer file.Close()

        len, err := file.WriteString("0")
        if err != nil {
                log.Fatalf("failed writing to file: %s", err)
        }
	fmt.Printf("Len : %s",len)


}
func ReadFile(){
        f, err := os.Open("flag.txt")
    
        if err != nil {
            log.Fatal(err)
        }
        // remember to close the file at the end of the program
        defer f.Close()
    
        // read the file line by line using scanner
        scanner := bufio.NewScanner(f)
    
        for scanner.Scan() {
            if scanner.Text() != "0"{
                fmt.Printf("line: %s\n", scanner.Text())
                modNumber =4
            }else{
                modNumber=3
            }
        }   
}

func proxy(backend string , c net.Conn) error{

        bc,err := net.Dial("tcp",backend)
        if err != nil {
                return fmt.Errorf("failed to connect to backend %s %v",backend,err)
        }


        go io.Copy(bc , c)

        go io.Copy(c,bc)

        return nil
}

func chooseBackend() string {
        counter ++
        ReadFile()
        return server[counter%modNumber]
}
    
