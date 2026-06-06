import { NextResponse } from "next/server"
import dbConnect from "@/lib/mongodb"
import User from "@/models/User"

export async function POST(req: Request) {
  try {
    await dbConnect()

    const body = await req.json()
    const { email } = body

    if (!email) {
      return NextResponse.json(
        { error: "Email is required" },
        { status: 400 }
      )
    }

    const user = await User.findOne({ email })

    if (!user) {
      return NextResponse.json(
        { error: "User not found" },
        { status: 404 }
      )
    }

    const userData = {
      _id: user._id,
      email: user.email,
      name: user.name,
      monthlyCarbon: user.monthlyCarbon || 0,
      totalScanned: user.totalScanned || 0,
      joinedAt:
        user.createdAt?.toISOString().split("T")[0] ||
        new Date().toISOString().split("T")[0],
    }

    return NextResponse.json({ user: userData }, { status: 200 })
  } catch (error) {
    const message =
      error instanceof Error ? error.message : "Unknown server error"

    return NextResponse.json(
      { error: message },
      { status: 500 }
    )
  }
}