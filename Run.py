try:
    import requests, json, socks, socket, re, base64, sys, os, time, datetime, threading
    from concurrent.futures import ThreadPoolExecutor
    from rich.console import Console
    from rich import print as printf
    from bs4 import BeautifulSoup
    from rich.panel import Panel
    from rich.columns import Columns
    from requests.exceptions import RequestException
except (ModuleNotFoundError) as e:
    __import__("sys").exit(f"[Error] {str(e).capitalize()}!")

DUMP = []


class FEATURE:
    def __init__(self):
        try:
            os.system("cls" if os.name == "nt" else "clear")
            printf(
                Panel(
                    r"""[bold red]  _____                     _    _             _            
 |  __ \                   | |  | |           | |           
 | |__) | __ _____  ___   _| |__| |_   _ _ __ | |_ ___ _ __ 
 |  ___/ '__/ _ \ \/ / | | |  __  | | | | '_ \| __/ _ \ '__|
 | |   | | | (_) >  <| |_| | |  | | |_| | | | | ||  __/ |   
[bold white] |_|   |_|  \___/_/\_\\__, |_|  |_|\__,_|_| |_|\__\___|_|   
                       __/ |                                
                      |___/                                 
         [bold white][+] [underline white red]Scraper and Validator - by Rozhak[/][bold white] [+]""",
                    width=65,
                    style="bold bright_black",
                )
            )

            try:
                with requests.Session() as SESSION:
                    SESSION.headers.update(
                        {
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Host": "ipinfo.io",
                            "Sec-Fetch-Dest": "document",
                            "Sec-Fetch-User": "?1",
                            "Sec-Fetch-Site": "none",
                            "Sec-Fetch-Mode": "navigate",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                        }
                    )
                    RESPONSE = json.loads(SESSION.get("https://ipinfo.io/json").text)
                    self.IP, self.CITY = (RESPONSE["ip"], RESPONSE["city"])
            except:
                self.IP, self.CITY = ("null", "null")

            printf(
                Columns(
                    [
                        Panel(
                            f"[bold white]IP :[bold green] {self.IP}",
                            width=32,
                            style="bold bright_black",
                        ),
                        Panel(
                            f"[bold white]City :[bold green] {self.CITY}",
                            width=32,
                            style="bold bright_black",
                        ),
                    ]
                )
            )
            printf(
                Panel(
                    f"""[bold green]01[bold white]. Scrape from Proxyscrape      [bold green]07[bold white]. Scrape from Proxy-Elite
[bold green]02[bold white]. Scrape from Freeproxy        [bold green]08[bold white]. Scrape from Hidemy-Life
[bold green]03[bold white]. Scrape from Proxy-Org        [bold green]09[bold white]. Scrape from Proxy-List
[bold green]04[bold white]. Scrape from Spys-Me          [bold green]10[bold white]. Scrape from Proxydocker
[bold green]05[bold white]. Scrape from Sslproxies       [bold green]11[bold white]. Check Live or Die
[bold green]06[bold white]. Scrape from Free-List        [bold green]12[bold white]. Logout from Program""",
                    width=65,
                    style="bold bright_black",
                    title="[bold bright_black]> [Feature] <",
                    subtitle="[bold bright_black]╭───────",
                    subtitle_align="left",
                )
            )
            self.CHOOSE = Console().input(f"[bold bright_black]   ╰─> ")
            if self.CHOOSE in ["01", "1"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )

                CLASS = SCRAPE()
                CLASS.PROXYSCRAPE_COM()

                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["02", "2"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                printf(
                    Panel(
                        f"[bold white]You must fill in the number of pages on the proxy scrape, make sure it is more than 1 so that it can be\nprocessed. For example:[bold green] 10[bold white] *[bold red]remember to use only numbers[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Page Count] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.COUNT = int(Console().input(f"[bold bright_black]   ╰─> "))

                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )
                for PAGES in range(1, int(self.COUNT) + 1):
                    CLASS = SCRAPE()
                    CLASS.FREEPROXY_WORLD(pages=PAGES)
                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["03", "3"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                printf(
                    Panel(
                        f"[bold white]You must fill in the number of pages on the proxy scrape, make sure it is more than 1 so that it can be\nprocessed. For example:[bold green] 10[bold white] *[bold red]remember to use only numbers[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Page Count] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.COUNT = int(Console().input(f"[bold bright_black]   ╰─> "))

                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )
                for PAGES in range(1, int(self.COUNT) + 1):
                    CLASS = SCRAPE()
                    CLASS.PROXY_LIST_ORG(pages=PAGES)
                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["04", "4"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )

                CLASS = SCRAPE()
                CLASS.SPYS_ME()

                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["05", "5"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )

                CLASS = SCRAPE()
                CLASS.SSLPROXIES_ORG()

                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["06", "6"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                printf(
                    Panel(
                        f"[bold white]You must fill in the number of pages on the proxy scrape, make sure it is more than 1 so that it can be\nprocessed. For example:[bold green] 10[bold white] *[bold red]remember to use only numbers[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Page Count] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.COUNT = int(Console().input(f"[bold bright_black]   ╰─> "))

                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )
                for PAGES in range(1, int(self.COUNT) + 1):
                    CLASS = SCRAPE()
                    CLASS.FREEPROXYLIST_CC(pages=self.COUNT)
                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["07", "7"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                printf(
                    Panel(
                        f"[bold white]You must fill in the number of pages on the proxy scrape, make sure it is more than 1 so that it can be\nprocessed. For example:[bold green] 10[bold white] *[bold red]remember to use only numbers[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Page Count] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.COUNT = int(Console().input(f"[bold bright_black]   ╰─> "))

                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )
                with requests.Session() as SESSION:
                    SESSION.headers.update(
                        {
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Host": "proxyelite.info",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-Site": "none",
                            "Sec-Fetch-User": "?1",
                            "Sec-Fetch-Dest": "document",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                        }
                    )
                    RESPONSE = SESSION.get("https://proxyelite.info/free-proxy-list/")
                    self.NONCE = re.search(
                        r'"nonce":"(.*?)"', str(RESPONSE.text)
                    ).group(1)
                for PAGES in range(1, int(self.COUNT) + 1):
                    CLASS = SCRAPE()
                    CLASS.PROXYELITE_INFO(
                        session=SESSION, pages=PAGES, nonce=self.NONCE
                    )
                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["08", "8"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )

                CLASS = SCRAPE()
                CLASS.HIDEMY_LIVE()

                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["09", "9"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")
                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )

                CLASS = SCRAPE()
                CLASS.PROXY_LIST_DOWNLOAD()

                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["10"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file name to save your proxy, check the file is correct before entering. For example:[bold green] Penyimpanan/Proxy.txt[bold white] *[bold red]make sure there is access to write[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")

                self.WRITE_NULL(files=self.FILES)
                printf(
                    Panel(
                        f"[bold white]While collecting all available Proxies, you can use[bold green] CTRL + C[bold white] to stop, remember not to use[bold red] CTRL + Z[bold white] to save the Proxies!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )
                with requests.Session() as SESSION:
                    SESSION.headers.update(
                        {
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-Site": "none",
                            "Sec-Fetch-User": "?1",
                            "Sec-Fetch-Dest": "document",
                            "Host": "www.proxydocker.com",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                        }
                    )
                    RESPONSE = SESSION.get("https://www.proxydocker.com/")
                    self.COOKIES = "; ".join(
                        [
                            str(key) + "=" + str(value)
                            for key, value in SESSION.cookies.get_dict().items()
                        ]
                    )
                    self._TOKEN = re.search(
                        'name="_token" content= "(.*?)"', str(RESPONSE.text)
                    ).group(1)

                CLASS = SCRAPE()
                CLASS.PROXYDOCKER_COM(
                    session=SESSION, cookies=self.COOKIES, _token=self._TOKEN
                )

                self.WRITE_PROXY(files=self.FILES)
                sys.exit()
            elif self.CHOOSE in ["11"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the file that contains the proxy list, make sure the file is available. For example:[bold green] Penyimpanan/Prox\ny.txt[bold white] *remember the ip and proxy separator must be a[bold red] colon[bold white]!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [File Name] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILES = Console().input(f"[bold bright_black]   ╰─> ")

                printf(
                    Panel(
                        f"[bold white]You must choose to use https to validate whether the proxy is valid or not, type[bold green] Y[bold white] if you want to use https otherwise\ntype[bold red] N[bold white]. For example:[bold green] Y[bold white] *[bold yellow]remember there are only two choices!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Protocol] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.CHOICES = Console().input(f"[bold bright_black]   ╰─> ")

                printf(
                    Panel(
                        f"[bold white]While checking proxy live or dead, you can use[bold red] CTRL + Z[bold white] to stop and make sure your connection is good!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Warning] <",
                    )
                )
                CHECKER().THREAD_POOL_EXECUTOR(
                    files=self.FILES, _type=self.CHOICES.upper() == "Y"
                )
            elif self.CHOOSE in ["12"]:
                printf(
                    Panel(
                        f"[bold white]Thank you for using this program, you are now successfully logged out!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Leave] <",
                    )
                )
                sys.exit()
            else:
                printf(
                    Panel(
                        f"[bold red]The option you entered is not available in the Features, please try another option!",
                        width=65,
                        style="bold bright_black",
                        title="[bold bright_black]> [Wrong Choice] <",
                    )
                )
                time.sleep(4.5)
                FEATURE()
        except (Exception) as e:
            printf(
                Panel(
                    f"[bold red]{str(e).capitalize()}!",
                    width=65,
                    style="bold bright_black",
                    title="[bold bright_black]> [Error] <",
                )
            )
            sys.exit()

    def WRITE_PROXY(self, files):
        if len(DUMP) >= 1 and len(DUMP) != 0:
            printf(
                f"[bold bright_black]   ──>[bold green] WRITE PROXY TO FILE!                 ",
                end="\r",
            )
            time.sleep(2.5)
            for LIST in DUMP:
                with open(f"{files}", "a+") as W:
                    W.write(f"{LIST}\n")
            printf(
                Panel(
                    f"""[bold white]Status :[bold green] Successfully saved all Proxies!
[bold white]Proxy Count :[bold yellow] {len(DUMP)}[bold white] /[bold yellow] {len(open(files, 'r').readlines())}
[bold white]Files :[bold red] {files}""",
                    width=65,
                    style="bold bright_black",
                    title="[bold bright_black]> [Sukses] <",
                )
            )
            return True
        else:
            printf(
                Panel(
                    f"[bold red]Didn't find any Proxy from this service, please try again later or try using another service!",
                    width=65,
                    style="bold bright_black",
                    title="[bold bright_black]> [Empty Proxy] <",
                )
            )
            return False

    def WRITE_NULL(self, files):
        with open(f"{files}", "w+") as W:
            W.write("")
        W.close()
        return True


class CHECKER:
    def __init__(self) -> None:
        self.PROXY_TYPES = ["http", "https", "socks4", "socks5"]
        self.LOCK = threading.Lock()
        self.LIVE = []
        self.DIE = []
        self.LOOPING = 0

    def WRITE_RESULTS(self, type_, proxies):
        self.TIMES_NOW = datetime.datetime.now()
        self.FILE_PATH = self.TIMES_NOW.strftime(
            f"Temporary/{type_.capitalize()}-%d-%m-%Y.txt"
        )

        with open(self.FILE_PATH, "a") as W:
            W.write(f"{proxies}\n")
        return True

    def THREAD_POOL_EXECUTOR(self, files, _type):
        PROXIES_LIST = open(f"{files}", "r").read().strip().splitlines()

        def PROCESS_PROXY(PROXY):
            IP, PORT = PROXY.split(":")

            FOUND_LIVE = False
            for PROXY_TYPE in self.PROXY_TYPES:
                if self.PROXY(IP, PORT, proxy_type=PROXY_TYPE, _type=_type):
                    with self.LOCK:
                        self.LIVE.append(f"{IP}:{PORT}")
                        self.WRITE_RESULTS("LIVE", f"{IP}:{PORT}")
                        FOUND_LIVE = True
                    break

            if not FOUND_LIVE:
                with self.LOCK:
                    self.DIE.append(f"{IP}:{PORT}")
                    self.WRITE_RESULTS("DIE", f"{IP}:{PORT}")

            with self.LOCK:
                self.LOOPING += 1
                printf(
                    f"[bold bright_black]   ──>[bold white] CHECK[bold blue] {str(IP)}[bold white]/[bold blue]{self.LOOPING}[bold white]/[bold blue]{len(PROXIES_LIST)}[bold white] LIVE:-[bold green]{len(self.LIVE)}[bold white] DIE:-[bold red]{len(self.DIE)}[bold white]     ",
                    end="\r",
                )

        with ThreadPoolExecutor(max_workers=20) as EXECUTOR:
            EXECUTOR.map(PROCESS_PROXY, PROXIES_LIST)

        printf(
            Panel(
                f"""[bold white]Status :[bold green] Successfully saved all Proxies!
[bold white]Live or Die :[bold green] {len(self.LIVE)}[bold white] /[bold red] {len(self.DIE)}
[bold white]Files :[bold yellow] {datetime.datetime.now().strftime(f"Temporary/Live-%d-%m-%Y.txt")}""",
                width=65,
                style="bold bright_black",
                title="[bold bright_black]> [Sukses] <",
            )
        )
        sys.exit()

    def PROXY(self, ip_address, port, proxy_type="http", _type=False):
        try:
            if proxy_type in ["http", "https"]:
                proxies = {
                    PROTOCOL: f"{proxy_type}://{ip_address}:{port}"
                    for PROTOCOL in ["http", "https"]
                }
                if bool(_type) == True:
                    self.URL, self.VERIFY = (
                        "https://icanhazip.com/",
                        True,
                    )  # https://httpbin.org/ip
                else:
                    self.URL, self.VERIFY = (
                        "http://icanhazip.com/",
                        False,
                    )  # http://httpbin.org/ip
                RESPONSE = requests.get(
                    "{}".format(self.URL),
                    proxies=proxies,
                    timeout=10,
                    verify=self.VERIFY,
                )
                return RESPONSE.status_code == 200 and ip_address in RESPONSE.text

            elif proxy_type == "socks4":
                socks.set_default_proxy(socks.SOCKS4, ip_address, int(port))
            elif proxy_type == "socks5":
                socks.set_default_proxy(socks.SOCKS5, ip_address, int(port))
            else:
                return False

            socket.socket = socks.socksocket
            sock = socket.socket()
            sock.settimeout(10)
            sock.connect(("www.google.com", 80))
            sock.close()
            return True
        except Exception as e:
            return False


class SCRAPE:
    def __init__(self) -> None:
        pass

    def PROXYDOCKER_COM(self, session, cookies, _token):
        try:
            session.headers.update(
                {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://www.proxydocker.com",
                    "Cookie": "{}".format(cookies),
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Accept": "*/*",
                    "Sec-Fetch-Site": "same-origin",
                    "Referer": "https://www.proxydocker.com/",
                }
            )
            data = {
                "anonymity": "all",
                "need": "all",
                "city": "all",
                "token": f"{_token}",
                "state": "all",
                "page": "1",
                "port": "all",
                "type": "all",
                "country": "all",
            }
            RESPONSE = session.post(
                "https://www.proxydocker.com/en/api/proxylist/", data=data
            )
            if '"ip":' in str(RESPONSE.text) and '"port":' in str(RESPONSE.text):
                self.JSON_RESPONSE = json.loads(RESPONSE.text)
                for PROXIES in self.JSON_RESPONSE["proxies"]:
                    printf(
                        f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(PROXIES['ip'])}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                        end="\r",
                    )
                    time.sleep(0.007)
                    DUMP.append(f'{PROXIES["ip"]}:{PROXIES["port"]}')
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
            else:
                printf(
                    f"[bold bright_black]   ──>[bold red] NO VALID PROXY FOUND!                ",
                    end="\r",
                )
                time.sleep(3.5)
                return False
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.HIDEMY_LIVE()
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def PROXY_LIST_DOWNLOAD(self):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "Host": "www.proxy-list.download",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                    }
                )
                RESPONSE = SESSION.get(
                    "https://www.proxy-list.download/api/v2/get?l=en&t=http"
                )

                if '"IP":' in str(RESPONSE.text) and '"PORT":' in str(RESPONSE.text):
                    self.JSON_RESPONSE = json.loads(RESPONSE.text)
                    for PROXY in self.JSON_RESPONSE["LISTA"]:
                        printf(
                            f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(PROXY['IP'])}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                            end="\r",
                        )
                        time.sleep(0.0007)
                        DUMP.append(f'{PROXY["IP"]}:{PROXY["PORT"]}')
                    printf(
                        f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                        end="\r",
                    )
                    time.sleep(2.5)
                    return True
                else:
                    printf(
                        f"[bold bright_black]   ──>[bold red] NO VALID PROXY FOUND!                ",
                        end="\r",
                    )
                    time.sleep(3.5)
                    return False
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.HIDEMY_LIVE()
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def HIDEMY_LIVE(self):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Site": "none",
                        "Sec-Fetch-User": "?1",
                        "Host": "hidemy.life",
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-Mode": "navigate",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                    }
                )
                RESPONSE = SESSION.get("https://hidemy.life/en/proxy-list-servers")

                self.SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
                self.ROWS = self.SOUP.find_all("tr")

                for ROW in self.ROWS:
                    self.COLUMNS = ROW.find_all("td")
                    if len(self.COLUMNS) >= 2:
                        self.PORT = self.COLUMNS[1].text.strip()
                        self.IP = self.COLUMNS[0].text.strip()
                        if str(self.IP) not in DUMP:
                            printf(
                                f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(self.IP)}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                                end="\r",
                            )
                            time.sleep(0.0007)
                            DUMP.append(f"{self.IP}:{self.PORT}")
                        else:
                            continue
                    else:
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.HIDEMY_LIVE()
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def PROXYELITE_INFO(self, session, pages, nonce):
        try:
            data = {
                "action": "proxylister_load_more",
                "nonce": f"{nonce}",
                "page": f"{pages}",
                "atts[downloads]": "true",
            }
            session.headers.update(
                {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Content-Length": "{}".format(len(str(data))),
                    "Sec-Fetch-Site": "same-origin",
                    "Accept": "*/*",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                }
            )
            RESPONSE = session.post(
                "https://proxyelite.info/wp-admin/admin-ajax.php", data=data
            )
            if '"success":true,' in str(RESPONSE.text):
                self.JSON_RESPONSE = json.loads(RESPONSE.text)
                self.HTML_DATA = self.JSON_RESPONSE["data"]["rows"]

                self.SOUP = BeautifulSoup(self.HTML_DATA, "html.parser")
                self.ROWS = self.SOUP.find_all("tr")

                for ROW in self.ROWS:
                    self.IP = ROW.find("td", class_="table-ip").text.strip()
                    self.PORT = ROW.find_all("td")[1].text.strip()
                    if str(self.IP) not in DUMP:
                        printf(
                            f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(self.IP)}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                            end="\r",
                        )
                        time.sleep(0.007)
                        DUMP.append(f"{self.IP}:{self.PORT}")
                    else:
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
            else:
                printf(
                    f"[bold bright_black]   ──>[bold red] NO VALID PROXY FOUND!                ",
                    end="\r",
                )
                time.sleep(3.5)
                return False
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.PROXYELITE_INFO(session, pages=int(pages) + 1, nonce=nonce)
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def FREEPROXYLIST_CC(self, pages):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "freeproxylist.cc",
                        "Sec-Fetch-Site": "none",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-Mode": "navigate",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.",
                    }
                )
                RESPONSE = SESSION.get(
                    "https://freeproxylist.cc/servers/{}.html".format(pages)
                )

                self.SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
                self.ROWS = self.SOUP.find_all("tr")

                for ROW in self.ROWS:
                    self.COLUMNS = ROW.find_all("td")
                    if len(self.COLUMNS) >= 2:
                        self.PORT = self.COLUMNS[1].text.strip()
                        self.IP = self.COLUMNS[0].text.strip()
                        if str(self.IP) not in DUMP:
                            printf(
                                f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(self.IP)}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                                end="\r",
                            )
                            time.sleep(0.0007)
                            DUMP.append(f"{self.IP}:{self.PORT}")
                        else:
                            continue
                    else:
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.FREEPROXYLIST_CC(pages=int(pages) + 1)
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def SSLPROXIES_ORG(self):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "www.sslproxies.org",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Site": "none",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Dest": "document",
                    }
                )
                RESPONSE = SESSION.get("https://www.sslproxies.org/")

                self.SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
                self.TD_ELEMENTS = self.SOUP.find_all("td")

                for I in range(0, len(self.TD_ELEMENTS) - 1, 8):
                    self.PORT = self.TD_ELEMENTS[I + 1].get_text(strip=True)
                    self.IP = self.TD_ELEMENTS[I].get_text(strip=True)

                    if self.IS_VALID_IP(self.IP) and self.IS_VALID_PORT(self.PORT):
                        if str(self.IP) not in DUMP:
                            printf(
                                f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(self.IP)}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                                end="\r",
                            )
                            time.sleep(0.0007)
                            DUMP.append(f"{self.IP}:{self.PORT}")
                        else:
                            continue
                    else:
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.SSLPROXIES_ORG()
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def IS_VALID_IP(self, ip):
        self.PATTERN = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
        return self.PATTERN.match(ip) is not None

    def IS_VALID_PORT(self, port):
        return port.isdigit() and 0 < int(port) <= 65535

    def SPYS_ME(self):  # CloudFlare
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Site": "same-origin",
                        "Host": "proxy-list.org",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Dest": "document",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                    }
                )
                RESPONSE = SESSION.get("https://spys.me/proxy.txt")

                self.IP_PORT_PAIRS = re.findall(
                    r"(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5})", RESPONSE.text
                )
                for IP, PORT in self.IP_PORT_PAIRS:
                    if str(IP) not in DUMP:
                        printf(
                            f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(IP)}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                            end="\r",
                        )
                        time.sleep(0.0007)
                        DUMP.append(f"{IP}:{PORT}")
                    else:
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.SPYS_ME()
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def PROXY_LIST_ORG(self, pages):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Site": "same-origin",
                        "Host": "proxy-list.org",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Dest": "document",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                    }
                )
                RESPONSE = SESSION.get(
                    "https://proxy-list.org/english/index.php?p={}".format(pages)
                )

                self.PROXY = re.findall(r"Proxy\('(.*?)'\)", str(RESPONSE.text))
                for BASE64_STR in self.PROXY:
                    try:
                        self.DECODED_BYTES = base64.b64decode(BASE64_STR)
                        self.PROXIES = self.DECODED_BYTES.decode("utf-8")
                        if str(self.PROXIES) not in DUMP and ":" in str(self.PROXIES):
                            printf(
                                f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(self.PROXIES.split(':')[0])}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                                end="\r",
                            )
                            time.sleep(0.007)
                            DUMP.append(f"{self.PROXIES}")
                        else:
                            continue
                    except (Exception):
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.PROXY_LIST_ORG(pages=int(pages) + 1)
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def FREEPROXY_WORLD(self, pages):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "www.freeproxy.world",
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Site": "none",
                        "Sec-Fetch-Mode": "navigate",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                    }
                )
                RESPONSE = SESSION.get(
                    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={}".format(
                        pages
                    )
                )

                self.SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
                self.IP_ADDRESSES = self.SOUP.find_all("td", class_="show-ip-div")
                self.PORTS = [
                    TD.find_next_sibling("td").find("a").get_text(strip=True)
                    for TD in self.IP_ADDRESSES
                ]

                self.PROXIES = [
                    (IP.get_text(strip=True), PORT)
                    for IP, PORT in zip(self.IP_ADDRESSES, self.PORTS)
                ]
                for IP, PORT in self.PROXIES:
                    if str(IP) not in DUMP:
                        printf(
                            f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(IP)}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                            end="\r",
                        )
                        time.sleep(0.007)
                        DUMP.append(f"{IP}:{PORT}")
                    else:
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.FREEPROXY_WORLD(pages=int(pages) + 1)
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True

    def PROXYSCRAPE_COM(self):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update(
                    {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Site": "none",
                        "Sec-Fetch-User": "?1",
                        "Host": "api.proxyscrape.com",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                    }
                )
                RESPONSE = requests.get(
                    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text"
                )

                self.IP_PORT_PAIRS = re.findall(
                    r"(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5})", RESPONSE.text
                )
                for IP, PORT in self.IP_PORT_PAIRS:
                    if str(IP) not in DUMP:
                        printf(
                            f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(IP)}[bold white]/[bold green]{len(DUMP)}[bold white] PROXY!     ",
                            end="\r",
                        )
                        time.sleep(0.0007)
                        DUMP.append(f"{IP}:{PORT}")
                    else:
                        continue
                printf(
                    f"[bold bright_black]   ──>[bold green] DONE TAKING ALL PROXY!             ",
                    end="\r",
                )
                time.sleep(2.5)
                return True
        except (RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS HAVING A PROBLEM!     ",
                end="\r",
            )
            time.sleep(10.0)
            self.PROXYSCRAPE_COM()
        except (KeyboardInterrupt):
            printf(f"                           ", end="\r")
            return True


if __name__ == "__main__":
    try:
        os.makedirs("Temporary", exist_ok=True)
        os.system("git pull")
        FEATURE()
    except (KeyboardInterrupt):
        sys.exit()