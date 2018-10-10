<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Symfony\Component\Process\Process;
use Illuminate\Support\Facades\Storage;

class SubmitController extends Controller
{
    public function submit(Request $request){
        if ($request->input_file->isValid()) {
            $technique = $request->technique;
            $method = $request->compression_method;
            $uuid = uniqid();
            $path = $request->input_file->move(base_path('storage/upload'), "$uuid");
            $as_file = $request->as_file;

            $out = [];
            $status = 0;
            exec(
                "python ../storage/compressor/app.py $technique $method $path upload/$path 2>&1", $out, $status);

            $compression_ratio = floatval(implode('', $out)) * 100;

            if ($status == 0) {
                if ($as_file)
                    return response()->download(storage_path("upload/$uuid.output"));
                else
                    return "compression ratio: $compression_ratio% <a href=\"/storage/$uuid.output\">download</a>";
            }
            abort(500);
        }
    }
}
