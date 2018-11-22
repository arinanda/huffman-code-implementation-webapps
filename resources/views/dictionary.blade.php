<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Colorlib Templates">
    <meta name="author" content="Colorlib">
    <meta name="keywords" content="Colorlib Templates">

    <!-- Title Page-->
    <title>Dictionary Coding</title>

    <!-- Icons font CSS-->
    <link href="vendor/mdi-font/css/material-design-iconic-font.min.css" rel="stylesheet" media="all">
    <link href="vendor/font-awesome-4.7/css/font-awesome.min.css" rel="stylesheet" media="all">
    <!-- Font special for pages-->
    <link href="https://fonts.googleapis.com/css?family=Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

    <!-- Vendor CSS-->
    <link href="vendor/select2/select2.min.css" rel="stylesheet" media="all">
    <link href="vendor/datepicker/daterangepicker.css" rel="stylesheet" media="all">

    <!-- Main CSS-->
    <link href="css/main.css" rel="stylesheet" media="all">
</head>

<body>
<div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
    <div class="wrapper wrapper--w680">
        <div class="card card-4">
            <div class="card-body">
                <h2 class="title">Dictionary Coding Implementation</h2>
                <form method="post" action="{{url('/submit')}}" enctype="multipart/form-data">

                    {{ csrf_field() }}

                    <div class="input-group">
                        <label class="label">Input File</label>
                        <input class="" type="file" name="input_file">
                    </div>

                    <div class="input-group">
                        <label class="label">Mode</label>
                        <div class="p-t-10">
                            <label class="radio-container m-r-45">Compress
                                <input type="radio" name="mode" value="compress">
                                <span class="checkmark"></span>
                            </label>
                            <label class="radio-container">Decompress
                                <input type="radio" name="mode" value="decompress">
                                <span class="checkmark"></span>
                            </label>
                        </div>
                    </div>

                    <div class="input-group">
                        <label class="label">Method</label>
                        <div class="rs-select2 js-select-simple select--no-search">
                            <select name="technique">
                                <option disabled="disabled" selected="selected">Choose option</option>
                                <option value="lzss">LZSS</option>
                                <option value="lzw">LZW</option>
                            </select>
                            <div class="select-dropdown"></div>
                        </div>
                    </div>

                    <div class="input-group">
                        <label class="label">Response Type</label>
                        <div class="p-t-10">
                            <label class="radio-container m-r-45">File
                                <input type="radio" name="response" value="file">
                                <span class="checkmark"></span>
                            </label>
                            <label class="radio-container">Compression Ratio
                                <input type="radio" name="response" value="compression_ratio">
                                <span class="checkmark"></span>
                            </label>
                        </div>
                    </div>

                    <div class="p-t-15">
                        <button class="btn btn--radius-2 btn--blue" type="submit">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Jquery JS-->
<script src="vendor/jquery/jquery.min.js"></script>
<!-- Vendor JS-->
<script src="vendor/select2/select2.min.js"></script>
<script src="vendor/datepicker/moment.min.js"></script>
<script src="vendor/datepicker/daterangepicker.js"></script>

<!-- Main JS-->
<script src="js/global.js"></script>

</body>
</html>
<!-- end document-->