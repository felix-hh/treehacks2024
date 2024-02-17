/**
 * v0 by Vercel.
 * @see https://v0.dev/t/lXda1I7GD1M
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import { CardTitle, CardDescription, CardHeader, CardContent, CardFooter, Card } from "@/components/ui/card"
import { Textarea } from "@/components/ui/textarea"
import { Button } from "@/components/ui/button"

export default function Component() {
  return (
    <Card className="w-full max-w-lg">
      <CardHeader>
        <CardTitle className="text-xl">Question 1</CardTitle>
        <CardDescription>You can answer this question in your own words.</CardDescription>
      </CardHeader>
      <CardContent className="grid gap-4">
        <p>What is your favorite color and why?</p>
        <div className="flex items-center space-x-2">
          <Textarea className="max-h-[100px] w-full resize-none text-base" placeholder="Type your response here." />
          <div className="text-sm font-medium peer">0 / 100</div>
        </div>
      </CardContent>
      <CardFooter>
        <div className="flex w-full justify-between">
          <Button variant="ghost">Previous</Button>
          <Button>Next</Button>
        </div>
      </CardFooter>
    </Card>
  )
}

