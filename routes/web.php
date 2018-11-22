<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::view('/huffman', 'huffman');
Route::view('/arithmetic', 'arithmetic');
Route::view('/dictionary', 'dictionary');
Route::post('/submit', 'SubmitController@submit');