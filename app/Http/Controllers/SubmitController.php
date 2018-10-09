<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Symfony\Component\Process\Process;
use Illuminate\Support\Facades\Storage;

class SubmitController extends Controller
{
    public function submit(Request $request){
        $path = $request->file('file')->storeAs('public', 'sample.txt');
        $todo = $request->todo;
        $method = $request->method;

        if($todo == "1" && $method == "1")
        {
            $process = new Process('python /storage/useHuffman.py');
            $process->run();
            return ($process->getOutput());    
        }
    }
}