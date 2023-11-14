import 'package:flutter/material.dart';
import 'package:ayurleaf/pages/login2.dart';
import 'package:ayurleaf/pages/login3.dart';
import 'package:ayurleaf/pages/homepage.dart';

class Login1 extends StatefulWidget {
  const Login1({super.key});

  @override
  State<Login1> createState() => _Login1State();
}

class _Login1State extends State<Login1> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body:
      Row(
        children: [
          Text("log in"),
          Text("Sign up"),
          Text("Continue without login")
        ],
      ),
    );
  }
}
