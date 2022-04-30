const root = document.querySelector("#root");

const upload = () => {
    const submit = document.querySelector("input[type='submit']");

    submit.addEventListener("click", async () => {
        // s3
        const resp = await fetch("/api/s3upload", {
            method: "PATCH",
            body: form,
        });

        // rds
    });
};

const download = () => {};

const initLoding = () => {};

initLoding();
