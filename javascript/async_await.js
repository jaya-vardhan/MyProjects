async function f1() {
    let sum = 0
    for (let i = 0; i < 10000; i++) {
        sum += i
    }
    return sum
}

// console.log(1)
// setTimeout(() => {
//     let r = f1()
//     console.log(r)
// }, 1000)

// console.log(2)
// setTimeout(() => {
//     let r = f1()
//     console.log(r)
// }, 1000)
// console.time("sync")
// console.log(3)
// // let res = f1()
// f1().then((res) => {
//     console.log(res)
// }, (error) => {
//     console.log("error")
// })
// // console.log(res)
// console.log(3)
// // let res1 = f1()
// f1().then((res) => {
//     console.log(res)
// }, (error) => {
//     console.log("error")
// })
// // console.log(res1)
// console.timeEnd("sync")
console.log(1)
async function f2() {
    f1().then((res) => {
        console.log("ddd::", res)
    }, (error) => {
        console.log("error")
    })
    console.log("jsjjsj")
    let res = await f1()
    console.log("res::", res)
    // console.log("1111")

    console.log("333")
}
f2()
console.log(2)

