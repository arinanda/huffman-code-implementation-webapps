<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SubmitController extends Controller
{
    private $PYTHON_COMMAND = 'python ../storage/compressor/app.py';
    private $STORAGE_PATH = 'storage/upload';

    public function submit(Request $request) {
        if ($request->input_file->isValid()) {
            $technique = $request->technique;
            $method = $request->mode;
            $uuid = uniqid();
            $path = $request->input_file->move(base_path($this->STORAGE_PATH), "$uuid");
            $response = $request->response;

            $out = [];
            $status = 0;
            $command = "$this->PYTHON_COMMAND $technique $method $path 2>&1";
            exec($command, $out, $status);
            $out = implode('', $out);

            $compression_ratio = floatval($out) * 100;

            if ($status == 0) {
                if ($response == 'file')
                    return response()->download(storage_path("upload\\$uuid.output"));
                else if ($response == 'compression_ratio')
                    abort(200, "Compression Ratio: $compression_ratio%");
                else
                    abort(200, 'Unknown response mode');
            }

            abort(200, $out);
        }

        abort(200, 'Invalid input file');
        return null;
    }
}
