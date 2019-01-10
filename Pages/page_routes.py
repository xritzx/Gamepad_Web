class Pages():
    def __init__(self):
        
        self.homepage = '''
        
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>Moto</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    html    {
                        height: 100%;
                    }
                    body    {
                        background: white;
                        height: 100%;
                    }
                    .stl    {
                        color: black;
                        font-size: 20px;
                        border: 5px wheat solid;
                        border-radius: 10%;
                        margin: 100px;
                        transform: rotate(90deg);
                    }
                    #down   {
                        padding: 100px;
                        position: absolute;
                    }
                    #up    {
                        float: right;
                        padding: 100px 150px;
                    }
                    #left  {
                        position: fixed;
                        bottom: 400px;
                        padding: 100px;
                    }
                    #right  {
                        position: fixed;
                        bottom: 10px;
                        padding: 100px;
                    }
                    </style>
            </head>
            <body>
                
                <div>
                    <button id="down" class="stl">DOWN</button>
                    <button id="up" class="stl">UP</button>
                </div>
                <div>
                    <button id="left" class="stl">LEFT</button>
                    <button id="right" class="stl">RIGHT</button>
                </div>
                <script>
                function movement(move) {
                    var req_param=String(move);
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = function() {
                        if (this.readyState == 4 && this.status == 200) {
                            var value = String(this.responseText);
                        }
                    };
                    xhttp.open("GET", req_param, true);
                    xhttp.send();
                }
                var up = document.querySelector("#up");
                var down = document.querySelector("#down");
                var left = document.querySelector("#left");
                var right = document.querySelector("#right");
                up.addEventListener("touchstart", ()=>{
                    movement("up");
                });
                up.addEventListener("touchend", ()=>{
                    movement("stop");
                });
                down.addEventListener("touchstart", ()=>{
                    movement("down");
                });
                down.addEventListener("touchend", ()=>{
                    movement("stop");
                });
                left.addEventListener("touchstart", ()=>{
                    movement("left");
                });
                left.addEventListener("touchend", ()=>{
                    movement("stop");
                });
                right.addEventListener("touchstart", ()=>{
                    movement("right");
                });
                right.addEventListener("touchend", ()=>{
                    movement("stop");
                });
                </script>
            </body>
        </html>

        '''